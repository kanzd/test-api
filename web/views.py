from django.shortcuts import render

# Create your views here.

from django.http import *
from django.shortcuts import *
from rest_framework.views import APIView
from rest_framework.response import *
from rest_framework import status
from .serializers import *
from .models import *

class TestView(APIView):
    def post(self,req):
        data = req.data
        print(data)
        t=Testmodel()
        t.res=str(data)
        t.save()
        print(req.META)
        client_ip=req.META['REMOTE_ADDR']
        return Response(
           {"statusCode":"0000","message":"successfull","client_ip":client_ip}
        )