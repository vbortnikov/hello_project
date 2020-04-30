## hello_project
hello web application exports metric to Prometheus and Grafana, working in Kubernetes or docker compose

Тестовое задание: реализовать "Привет Мир" HTTP-приложение, которое отдает метрики в Prometheus. Метрики визуализируются в Grafana
./hello_app - само приложение на языке  Python (Django). Хранит состояние здоровья и готовности, которые можно изменять через web-интерфейс (javascript AJAX)

Запуск приложения - [manage.py](hello_app/hello_project/manage.py) runserver [address_to_bind:port_number]  
По умолчанию стартует и доступно по адресу ***http://localhost:8000***  
#####endpoints:  
/ - основная страница, отображает состояние приложения и позволяет его изменять.  
/ready - проверка готовности приложения  
/health - проверка здоровья приложения  
/metrics - тестовые метрики.   
Формируются как с использованием [Prometheus Python Client](https://github.com/prometheus/client_python), так и самостоятельно.  
