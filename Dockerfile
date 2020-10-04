FROM python:3

EXPOSE 8000
ENV PYTHONUNBUFFERED 1
WORKDIR /djangoProject

ADD djangoProject /djangoProject

COPY requirements.txt /app/requirements.txt

RUN python djangoProject/manage.py makemigrations

RUN python djangoProject/manage.py migrate

RUN pip install -r requirements.txt

COPY djangoProject /djangoProject




