from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from apps import views


urlpatterns = [
    # path(r'', views.index),
    path(r'', RedirectView.as_view(url='/index/')),
    path(r'index/', views.index,name='index'),
    path(r'login/', views.login,name='login'),
    path(r'register/', views.register,name='register'),



]

