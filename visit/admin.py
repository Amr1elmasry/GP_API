from django.contrib import admin
from .models import Place,Statue
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']
# Register your models here.
admin.site.register(Place)
admin.site.register(Statue)
