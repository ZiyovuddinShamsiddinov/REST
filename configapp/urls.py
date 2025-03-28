from django.contrib import admin
from django.urls import path

from configapp.views import *

urlpatterns = [
    #get,post
    path('movie_api/', movie_api),
    #put,patch,delete
    path('movie_detail/<slug:slug>/', movie_details),
]
