FROM python:3.8-slim-buster
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_ENV production
ENV DEBIAN_FRONTEND noninteractive

RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app/requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt && rm requirements.txt

COPY . /usr/src/app/