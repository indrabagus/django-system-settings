from django.conf.urls import url
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from .views import LinuxSysInfo,DjangoSettings

urlpatterns = [
    url(r'^$',RedirectView.as_view(pattern_name='website:linuxsysinfo')),    
    url(r'^linuxsysinfo/$',LinuxSysInfo.as_view(),name='linuxsysinfo'),
    url(r'^djangosettings/$',DjangoSettings.as_view(),name='djangosettings'),    
    url(r'^login/$',auth_views.login,{'template_name': 'sysinfo_website/login.html'},name='login'),
    url(r'^logout/$',auth_views.logout,{'next_page': '/'},name='logout'),
]