from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #configapp api
    path('api/', include("configapp.urls")),
]
