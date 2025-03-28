from django.contrib import admin
from django.urls import path

from configapp.views import *

urlpatterns = [
    #get,post
    path('movie_api/', movie_api),
    #put,patch,delete
    path('movie_detail/<slug:slug>/', movie_detail),
    # get,post
    path('Actor_api/', actor_api),
    # put,patch,delete
    path('actor_detail/<slug:slug>/', actor_detail),

]
