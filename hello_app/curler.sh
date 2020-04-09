# helper to score up metrics
curl  -c cookies.txt -b cookies.txt -s -w "%{http_code}" http://localhost:8000/
token=$(grep srftoken cookies.txt | cut -f 7)
echo  "X-CSRFToken:${token}"
curl -c cookies.txt -b cookies.txt -s -H "X-CSRFToken:${token}" -w "%{http_code}"  -X POST http://localhost:8000/metrics/
curl -c cookies.txt -b cookies.txt -s -H "X-CSRFToken:${token}" -w "%{http_code}"  -X POST http://localhost:8000/ready/
curl -c cookies.txt -b cookies.txt -s -H "X-CSRFToken:${token}" -w "%{http_code}"  -X POST http://localhost:8000/health/

