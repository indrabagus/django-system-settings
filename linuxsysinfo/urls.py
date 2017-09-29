from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from linuxsysinfo import views

urlpatterns = [
    url(r'^api/sysinfo/$',views.LinuxSysInfoView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns, suffix_required=True,allowed=['json','api'])
# urlpatterns = format_suffix_patterns(urlpatterns)