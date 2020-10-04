FROM python:3

EXPOSE 8000
ENV PYTHONUNBUFFERED 1
WORKDIR /djangoProject

ADD djangoProject /djangoProject

COPY djangoProject/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY djangoProject /djangoProject




