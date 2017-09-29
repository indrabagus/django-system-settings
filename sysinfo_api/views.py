from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .settingmodels import LinuxSysInfo
from .serializers import LinuxSysInfoSerializer
# Create your views here.

class LinuxSysInfoView(APIView):
    def get(self,request,format=None):
        sysinfo = LinuxSysInfo()
        serializer = LinuxSysInfoSerializer(sysinfo)
        return Response(status=status.HTTP_200_OK,data=serializer.data)