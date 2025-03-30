FROM python:3.11-slim

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt


COPY ./start-web-dev /start-web-dev
RUN sed -i 's/\r$//g' /start-web-dev
RUN chmod +x /start-web-dev