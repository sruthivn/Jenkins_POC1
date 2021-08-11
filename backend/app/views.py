from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class Home(APIView):
    # permission_classes = (IsAuthenticated, )
    def get(self,request):
        response="Hello World"
        return Response(response)