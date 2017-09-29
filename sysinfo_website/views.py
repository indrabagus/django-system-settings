from django.shortcuts import render
from django.views import View
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# decorators = [login_required,never_cache]

class LinuxSysInfo(View):
    @method_decorator(login_required(login_url='website:login'))
    def get(self,request):
        return render(request,"sysinfo_website/linuxsysinfo.html")


@method_decorator(login_required(login_url='website:login'),name='get')    
class DjangoSettings(View):
    def get(self,request):
        return render(request,"sysinfo_website/linuxsysinfo.html")    
