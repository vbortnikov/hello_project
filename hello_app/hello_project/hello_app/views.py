from django.shortcuts import render
from django.http import HttpResponse
from prometheus_client import Counter
from prometheus_client import generate_latest
from prometheus_client import CONTENT_TYPE_LATEST

# my internal state in global scope
siteState = { "isHealthy" : True, "isReady" : True }
# using prometheus library here
httpCounter = Counter('hello_http_requests', 'Counter of HTTP requests', ['method','endpoint'])

# landing page: "hello world" + changing internal state with AJAX
def index(request):
    if request.method == "GET":
        httpCounter.labels(method='GET', endpoint='index').inc()
        return render(request, "index.html", context=siteState)

    # POST - from AJAX
    elif request.method == "POST":
        httpCounter.labels(method='POST', endpoint='index').inc()
        try:
            value = list(request.POST)[0]
        except(KeyError):
            return HttpResponse(status=404, reason="No key in POST")

        for item in siteState:
            if item == value:
                siteState[item] = not siteState[item]
                return HttpResponse(siteState[item], status=201)
        return HttpResponse(status=404, reason="Key not found in siteState dictionary")
    else:
        return HttpResponse(status=404, reason="Only GET and POST methods are allowed")


def metrics(request):
    import math
    import time
    healthMetric = (b"# HELP Let's show my health (boolean, 0.0 or 1.0)\n"
                    b"# TYPE hello_health gauge\n"
                    b"hello_health ")
    sinMetric = (b"# HELP Let's show math.sin() function\n"
                    b"# TYPE hello_sin gauge\n"
                    b"hello_sin ")
    httpCounter.labels(method='GET', endpoint='metrics').inc()

    # let the library works
    responseText = generate_latest()

    # and I can do almost the same
    responseText += healthMetric + bytes(str(float(siteState["isHealthy"])), "utf-8") + b'\n'
    responseText += sinMetric + bytes(str(math.sin(time.time()*5)), "utf-8") + b'\n'

    return HttpResponse(responseText, content_type = CONTENT_TYPE_LATEST)


def healthCheck(request):
    import json
    import os
    httpCounter.labels(method=request.method, endpoint='health').inc()

    # I hope Django will catch all my exceptions
    response = json.dumps({ "health": siteState["isHealthy"], "detail":{"osName" : os.name, "cpuCount": str(os.cpu_count()),"loadAverage" : str(os.getloadavg()) }})

    if siteState["isHealthy"]:
        return HttpResponse(response, status=200)
    else:
        return HttpResponse(response, status=500)


def readyCheck(request):
    httpCounter.labels(method=request.method, endpoint='ready').inc()
    if siteState["isReady"]:
        return HttpResponse("Ready", status=200)
    else:
        return HttpResponse("Just a moment...", status=500)
