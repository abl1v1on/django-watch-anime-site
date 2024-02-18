FROM python:3

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /temp/requirements.txt

COPY . /app

WORKDIR /app

# Открываем порт
EXPOSE 8000

RUN pip install --upgrade pip && pip install -r /temp/requirements.txt.
