FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN apk update && \
    apk add postgresql-dev musl-dev gcc postgresql && \
    pip install --no-cache-dir -r requirements.txt