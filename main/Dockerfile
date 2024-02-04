FROM python:3.10.0
ENV PYTHONUNBUFFERED 1
WORKDIR /flask
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /flask