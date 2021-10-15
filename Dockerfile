# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
ENV SECRET_KEY = "django-insecure-73c*bj-eq6!ru457i7(znh(ig)xo_@zct#oge\$ip_eug6l-r9d"
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/