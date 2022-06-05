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

    #English path
    path('api/en/statues/', views.CBV_StatuesEn.as_view()),
    path('api/en/places/<int:id>', views.CBV_Places_idEn.as_view()),

    path('api/en/places/', views.CBV_PlacesEn.as_view()),
    path('api/en/statues/<int:id>', views.CBV_Statues_idEn.as_view()),
    
    path('api/en/predict/', views.CBV_StatuePredict.as_view()),
    re_path(r'^api/en/statues/?place=(?P<place>.+)$', views.CBV_StatuePlaceEn.as_view()),


    #Arabic Path
    path('api/ar/statues/', views.CBV_StatuesAr.as_view()),
    path('api/ar/places/<int:id>', views.CBV_Places_idAr.as_view()),

    path('api/ar/places/', views.CBV_Places_idAr.as_view()),
    path('api/ar/statues/<int:id>', views.CBV_Statues_idAr.as_view()),


    re_path(r'^api/ar/statues/place=(?P<place>.+)$', views.CBV_StatuePlaceAr.as_view()),


    #Get key
    path('api/key/', obtain_auth_token)


] 