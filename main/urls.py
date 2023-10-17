from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('form', views.form),
    path('login', views.login),
]