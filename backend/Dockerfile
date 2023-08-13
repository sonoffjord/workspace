FROM python:3.10.12-alpine3.17

COPY requirements.txt /temp/requirements.txt

COPY code /code
WORKDIR /code
EXPOSE 8000

RUN pip install --upgrade pip && pip install -r /temp/requirements.txt

RUN adduser --disabled-password ws_user
USER ws_user
