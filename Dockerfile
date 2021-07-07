FROM python:3.9-alpine

MAINTAINER Vadym Khodak

COPY app.py /src/app.py
COPY requirements.txt /src/requirements.txt

WORKDIR /src

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
