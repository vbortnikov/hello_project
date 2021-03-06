# helper script (example) to score up metrics
# I need it because Django uses CSRFToken
curl  -c cookies.txt -b cookies.txt -s -w "%{http_code}" http://127.0.0.1:8000/
token=$(grep srftoken cookies.txt | cut -f 7)
echo  "X-CSRFToken:${token}"
curl -c cookies.txt -b cookies.txt -s -H "X-CSRFToken:${token}" -w "%{http_code}"  -X POST http://127.0.0.1:8000/metrics/
curl -c cookies.txt -b cookies.txt -s -H "X-CSRFToken:${token}" -w "%{http_code}"  -X POST http://127.0.0.1:8000/ready/
curl -c cookies.txt -b cookies.txt -s -H "X-CSRFToken:${token}" -w "%{http_code}"  -X POST http://127.0.0.1:8000/health/

