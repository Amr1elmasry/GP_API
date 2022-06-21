"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from visit import views
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import re_path



urlpatterns = [
    
    path('admin/', admin.site.urls),
    #Data path
    path('api/statues/', views.CBV_Statues.as_view()),
    path('api/places/<int:id>', views.CBV_Places_id.as_view()),

    path('api/places/', views.CBV_Places.as_view()),
    path('api/statues/<int:id>', views.CBV_Statues_id.as_view()),
    
    path('api/predict/<int:id>', views.CBV_StatuePredict.as_view()),
    re_path(r'^api/statues/?place=(?P<place>.+)$', views.CBV_StatuePlace.as_view()),
    re_path(r'^api/predict/?place=(?P<place>.+)$', views.CBV_StatuePredict.as_view()),

    #Get key
    path('api/key/', obtain_auth_token)


] 