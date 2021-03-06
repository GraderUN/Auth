FROM python:3

EXPOSE 8000
ENV PYTHONUNBUFFERED 1

WORKDIR /run

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

RUN pip3 install pyrebase4

RUN python manage.py makemigrations

RUN python manage.py migrate

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]





