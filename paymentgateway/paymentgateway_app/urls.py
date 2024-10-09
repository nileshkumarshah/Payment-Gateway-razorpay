from django.contrib import admin
from django.urls import path
from . import views

app_name = "paymentgateway_app"

urlpatterns = [
    path('', views.homepage, name='index'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
]
