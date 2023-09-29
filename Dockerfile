FROM --platform=$BUILDPLATFORM python:3.11-alpine AS builder
ENV PYTHONBUFFERED 1
EXPOSE 8000
WORKDIR .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN apk add py3-gunicorn
COPY . . 
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi"]
