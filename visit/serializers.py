from rest_framework import serializers
from visit.models import  Statue, Place



class PlaceSerialzerEnglish(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields  = ['id','name','description','images','lon','lat']

class StatueSerialzerEnglish(serializers.ModelSerializer):
    class Meta:
        model = Statue
        fields  = ['id','name','description','images','voice_over','place']


class PlaceSerialzerArabic(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields  = ['id','name_arabic','description_arabic','images','lon','lat']

class StatueSerialzerArabic(serializers.ModelSerializer):
    class Meta:
        model = Statue
        fields  = ['id','name_arabic','description_arabic','images','voice_over_arabic','place']

