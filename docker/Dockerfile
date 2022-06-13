FROM python:3.10.4-slim

RUN pip install -U pip
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY . /proj
WORKDIR /proj
