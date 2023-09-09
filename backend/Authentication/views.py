from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import serializers
from . serializers import MyUserRegistrationSerializer , MyUserLoginSerializer
from . models import MyUser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny ,IsAuthenticated
from django.utils.encoding import force_str

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_jwt.settings import api_settings
from .models import MyUser

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class MyUserRegistrationView(APIView):

    def post(self,request,format=None):
        serializer = MyUserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            MyUser = serializer.save()
            return Response({'msg':'User registered succesfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class MyUserLoginView(APIView):

    def post(self,request,format=None):

        serializer = MyUserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')

            user = authenticate(email=email,password=password)
            if user is not None:
                 return Response({'msg': f'Login success of user with id :- {user.id}'}, status=status.HTTP_200_OK)
            else:
                return Response({'msg':'User not found'},status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
