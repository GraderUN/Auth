from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']


class Token(models.Model):
    authToken = models.TextField(blank=False)


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = ['authToken']
