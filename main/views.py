from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.parsers import JSONParser

from .serializers import UserSerializer, TokenSerializer
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials

cred = credentials.Certificate("main/Keys/authgraderun-firebase-adminsdk.json")
firebase_admin.initialize_app(cred)


@csrf_exempt
def register(request):
    print("body", request)
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
    try:
        token = request.headers.get('Authorization')
        print(auth.verify_id_token(token))
        return HttpResponse('True')
    except:
        return HttpResponse('False')

@csrf_exempt
def updateEmail(request):
    data = JSONParser().parse(request)
    if request.method == 'PATCH':
        try:
            auth.update_user(data.get('userId'),
                             email=data.get('email'))
            return HttpResponse(True)
        except:
            return HttpResponse(False)


@csrf_exempt
def deleteUser(request):
    print("body", request)
    data = JSONParser().parse(request)
    if request.method == 'DELETE':
        try:
            auth.delete_user(data.get('userId'))
            return HttpResponse(True)
        except:
            return HttpResponse(False)
