FROM python:3.9-alpine

MAINTAINER Vadym Khodak

ADD . /src

WORKDIR /src

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
