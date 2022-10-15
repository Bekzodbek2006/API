from django.shortcuts import render

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token




# # API userset
# @api_view(["GET"])
# @permission_classes((permissions.AllowAny,))
# def contact_api(request):
#     api_urls = {
#         "List": "/contact-list/",
#         "Detail View": "/contact-detail/<str:pk>/",
#         "Create": "/contact-create/",
#         "Update": "/contact-update/<str:pk>/",
#         "Delete": "/contact-delete/<str:pk>",
#         "Taklif Filter": "/contact-taklif/",
#         "Shikoyat Filter": "/contact-shikoyat/",
#         "Search API": "/contact-search/",
#         "Order API": "/contact-order/",
#     }

#     return Response(api_urls)

# Class based view to Get User Details using Token Authentication
# class UserDetailAPI(APIView):
#   authentication_classes = (TokenAuthentication,)
#   permission_classes = (AllowAny,)
#   def get(self,request,*args,**kwargs):
#         user = User.objects.get(id=request.user.id)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

# #Class based view to register user
# class RegisterUserAPIView(generics.CreateAPIView):
#         permission_classes = (AllowAny,)
#         serializer_class = RegisterSerializer


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)