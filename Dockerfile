FROM python:3.10.7-buster

ENV PIP_NO_CACHE_DIR "true"

COPY ./requirements*.txt /code/

WORKDIR /code

RUN pip install -r requirements.txt -r requirements_dev.txt
