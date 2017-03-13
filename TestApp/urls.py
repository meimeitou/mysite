from django.conf.urls import url,include
from . import views
urlpatterns = [
   url(r'^testfile/$',views.files,name="upload"),
   url(r'^ths/$',views.ths,name="uploadths"),
]