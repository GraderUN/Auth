from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from .Keys import firebase
from .serializers import UserSerializer
import pyrebase


config = firebase.config
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


def signIn(request):
    data = JSONParser().parse(request)
    serialized = UserSerializer(data=data)
    if serialized.is_valid():
        try:
            auth.sign_in_with_email_and_password(serialized.data.get('email'),
                                                           serialized.data.get('password'))
            user =auth.current_user.get('idToken')
            return HttpResponse(user, "Registrado exitosamente")
        except:
            message = "invalid data"
            return HttpResponse(message, "ERROR FATAL, F EN EL CHAT")
