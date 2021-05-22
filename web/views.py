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
        
        return Response(
           {"statusCode":"0000","message":"successfull"}
        )