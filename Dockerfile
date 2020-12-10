FROM python:3.8.6-slim-buster

# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
RUN apt-get update && apt-get install -y \
    build-essential \
    vim \
    git \
    # for psycopg2 library
    libpq-dev \
    # for emails
    postfix \
    && apt-get clean

COPY requirements/ /app/requirements/

WORKDIR /app

ENV PYTHONPATH /app

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --requirement /app/requirements/dev.txt

CMD python3 manage.py runserver 0.0.0.0:8000
