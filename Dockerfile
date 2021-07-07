FROM python:3.9-alpine

MAINTAINER Vadym Khodak

COPY app.py /src/app.py
COPY requirements.txt /src/requirements.txt

WORKDIR /src

ENV REDIS_HOST: "redis"
ENV REDIS_PORT: 6379
ENV FLASK_HOST: "0.0.0.0"
ENV FLASK_PORT: 5000

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
