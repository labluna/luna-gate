from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^login/$', views.login, name='login'),
]

