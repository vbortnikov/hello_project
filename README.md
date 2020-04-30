## hello_project
hello web application exports metric to Prometheus and Grafana, working in Kubernetes or docker compose

Тестовое задание: реализовать "Привет Мир" HTTP-приложение, которое отдает метрики в Prometheus. Метрики визуализируются в Grafana

hello-app -> Prometheus -> Grafana  

### ./hello_app - приложение на языке  Python (Django).  
Хранит состояние здоровья и готовности, которые можно изменять через web-интерфейс (javascript AJAX)

Запуск приложения - [manage.py](hello_app/hello_project/manage.py) runserver [address_to_bind:port_number]  
По умолчанию стартует и доступно по адресу ***http://localhost:8000***  
##### endpoints:  
/ - основная страница, отображает состояние приложения и позволяет его изменять.  
/ready - проверка готовности приложения  
/health - проверка здоровья приложения  
/metrics - тестовые метрики.   
Метрики формируются как с использованием [Prometheus Python Client](https://github.com/prometheus/client_python), так и самостоятельно.  
backend, код Python находится в [views.py](hello_app/hello_project/hello_app/views.py)  
frontend, HTML+JavaScript - [index.html](hello_app/hello_project/hello_app/templates/index.html)  
### Запуск в Kubernets  
Текущая конфигурация тестировалась только под [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)  
Hello-app контейнезтровано и доступно через (Docker Hub)[https://hub.docker.com/repository/docker/vasily22/hello]  
Для Prometheus используется стандартный образ, без изменений (prom/prometheus:v2.17.1)[https://hub.docker.com/r/prom/prometheus]  
Grafana также стартует из стандартного образа (https://hub.docker.com/r/grafana/grafana)[grafana/grafana:6.7.2]  
ConfigMap c конфигурацией Prometheus монтирутся по стандартному пути _/etc//etc/prometheus/prometheus.yaml_  
Графана конфигурируется (DataSource & Dashboard) с помощью механизма Provisioning.  
В результате Datasource импортируется в БД с признаком read_only.  
(При необходимости это легко исправить напрямую в БД утилитой _sqlite3_)
