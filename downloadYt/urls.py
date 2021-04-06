from django.contrib import admin
from django.urls import path
from downloadYt import views

urlpatterns = [
    path('', views.index,name='downloadYt')
    # path('index', views.index,name='index'),

]