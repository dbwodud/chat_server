# chat/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index ,name='index'),
    url(r'^signup/$', views.signup , name='join'),
    url(r'^signin/$', views.signin , name='login')
]
