from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.parsers import JSONParser

from .serializers import UserSerializer, TokenSerializer
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from pyrebase import pyrebase

cred = credentials.Certificate("main/Keys/authgraderun-firebase-adminsdk.json")
firebase_admin.initialize_app(cred)


@csrf_exempt
def register(request):
    data = JSONParser().parse(request)
    serialized = UserSerializer(data=data)
    if serialized.is_valid():
        try:
            user = auth.create_user(
                email=serialized.data.get('email'),
                password=serialized.data.get('password')
            )
            print(user.email)
            message = 'Sucessfully created new user: '
            message += user.email
            return HttpResponse(message, "Registrado exitosamente")
        except:
            message = "invalid data"
            return HttpResponse(message, "ERROR FATAL, F EN EL CHAT")


def authRequest(request):
    data = JSONParser().parse(request)
    serialized = TokenSerializer(data=data)
    if serialized.is_valid():
        try:
            token = serialized.data.get('authToken')
            print(auth.verify_id_token(token))
            return HttpResponse('True')
        except:
            return HttpResponse('False')


def updateEmail(request):
    data = JSONParser().parse(request)
    try:
        auth.update_user(data.get('userId'),
                         email='saduquebe@unal.edu.er')
        return HttpResponse('Exito')
    except:
        return HttpResponse('No se pudo actualizar')


def deleteUser(request):
    data = JSONParser().parse(request)
    try:
        auth.delete_user(data.get('userId'))
        return HttpResponse('Exito')
    except:
        message = "No se pudo eliminar"
        return HttpResponse(message)
