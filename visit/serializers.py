from rest_framework import serializers
from visit.models import  Statue, Place



class PlaceSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields  = ['id','display_name','is_available','description','images','display_name_arabic','description_arabic','lon','lat','range']

class StatueSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Statue
        fields  = ['id','display_name','description','images','voice_over','display_name_arabic','description_arabic','voice_over_arabic','place']


