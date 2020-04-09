FROM python:3
ENV PYTHONUNBUFFERED 1
RUN pip install --no-cache-dir django prometheus_client
COPY . /hello
EXPOSE 8000/tcp
CMD [ "python", "/hello/manage.py", "runserver", "0.0.0.0:8000" ]