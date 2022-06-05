from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


# Create your models here.
class Place(models.Model):
   
   name = models.CharField(max_length= 100, null=True)
   description = models.TextField(max_length = 5000, null=True)
   images = ArrayField(models.URLField(max_length= 1000),size=3, default=list)
   #longitude and latitude values for location
   lon = models.DecimalField(max_digits=9, decimal_places=6, null=True)
   lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)


   name_arabic = models.CharField(max_length= 100, null=True)
   description_arabic = models.TextField(max_length = 5000, null=True)
 


class Statue(models.Model):
   
   name = models.CharField(max_length= 100, null=True)
   description = models.TextField(max_length = 5000, null=True)
   images = ArrayField(models.URLField(max_length= 1000),size=3, default=list)
   voice_over = models.URLField(max_length= 1000, null=True)
   place  = models.ForeignKey(Place, related_name='Place', on_delete=models.CASCADE, null=True)

   name_arabic = models.CharField(max_length= 100, null=True)
   description_arabic = models.TextField(max_length = 5000, null=True)
   voice_over_arabic = models.URLField(max_length= 1000, null=True)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)