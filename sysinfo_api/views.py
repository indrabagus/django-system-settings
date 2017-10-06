from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView,exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException, NotAuthenticated,PermissionDenied
from .settingmodels import LinuxSysInfo
from .serializers import LinuxSysInfoSerializer
# Create your views here.

    
def custom_exception_handler(exc,context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc,context)
    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['code'] = response.status_code
        response.data['status'] = response.status_text        
        response.data['error']=response.data.pop('detail')
    return response

class LinuxSysInfoView(APIView):
    def get(self,request,format=None):
        try:
            sysinfo = LinuxSysInfo()
            serializer = LinuxSysInfoSerializer(sysinfo)
            return Response(status=status.HTTP_200_OK,data=serializer.data)
        except NotAuthenticated as ex:
            print("Not Auth")