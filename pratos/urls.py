from django.urls import path
from . import views

urlpatterns=[
    path('', views.pratos, name='pratos')
]