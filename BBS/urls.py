__author__ = 'yinqiwei'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hellow/$',views.hello),
    url(r'^current[/]?$',views.current_datetime),
    url(r'^plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^time$',views.current_time),
    url(r'^time2$',views.curtent_time2)
]