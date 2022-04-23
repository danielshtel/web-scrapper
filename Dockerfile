FROM python:latest

WORKDIR /scrapper

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r /scrapper/requirements.txt

COPY . .
