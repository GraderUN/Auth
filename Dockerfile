FROM python:3

EXPOSE 8000
ENV PYTHONUNBUFFERED 1

WORKDIR /run

COPY requirements.txt ./

RUN pip install -r requirements.txt

RUN python manage.py makemigrations

RUN python manage.py migrate

COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]





