from rest_framework import serializers
from django.db import models


class User(models.Model):
    email = models.TextField(blank=False)
    password = models.CharField('password', max_length=128)
    role = models.CharField(blank=True,max_length=10)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'role']


class Token(models.Model):
    authToken = models.TextField(blank=False)


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['authToken']
