from contextvars import Token
import io
import os
import random
import string
from unicodedata import name
import cv2
import  keras
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse
from numpy import place
from PIL import Image
import requests
from matplotlib import image
from matplotlib.font_manager import json_dump
import numpy as np
import shutil
from .serializers import PlaceSerialzerArabic, PlaceSerialzerEnglish, StatueSerialzerArabic, StatueSerialzerEnglish
from .models import Statue, Place
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import TokenAuthentication   



classes_names = ['Amenhotep, Son of Hapu', 'Amenophis III his wife', 'Egyptian Writer', 'Hatshepsut', 'I Senwosert', 'III Senwosret', 'III Sphinxes of Amenemhat', 'Isis, mother of king Thutmose III', 'Khafre', 'Menkaure, Hathor and the gods', 'Narmer painting face 1', 'Narmer painting face 2', 'no name', 'Nofert', 'Pyramid', 'Rahotep', 'Rahotep and Nofret', 'Ramesses II usurped by Merenptah', 'Ramses II as a Standard Bearer', 'Sphinx']

#English Views

class CBV_PlacesEn(APIView):
    permission_classes = (IsAuthenticated,)  
    def get(self,request):
        places = Place.objects.all()
        serializer = PlaceSerialzerEnglish(places, many=True)
        return Response(serializer.data)

class CBV_Places_idEn(APIView):
    permission_classes = (IsAuthenticated,)  
    def get_object(self, id):
        try:
            return Place.objects.filter(id=id)
        except ObjectDoesNotExist:
            raise Http404

    def get(self,request,id):
        place = self.get_object(id)
        serializer = PlaceSerialzerEnglish(place, many=True)
        return Response(serializer.data)

class CBV_StatuesEn(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        statues = Statue.objects.all()
        serializer = StatueSerialzerEnglish(statues, many=True)
        return Response(serializer.data)

class CBV_Statues_idEn(APIView):
    permission_classes = (IsAuthenticated,)  
    def get_object(self, id):
        try:
            return Statue.objects.filter(id=id)
        except ObjectDoesNotExist:
            raise Http404

    def get(self,request,id):
        statue = self.get_object(id)
        serializer = StatueSerialzerEnglish(statue, many=True)
        return Response(serializer.data)

class CBV_StatuePlaceEn(APIView):
    permission_classes = (IsAuthenticated,)  
    def get_object(self, place):
        try:
            return Statue.objects.filter(place=place)
        except ObjectDoesNotExist:
            raise Http404

    def get(self,request,place):
        statue = self.get_object(place)
        serializer = StatueSerialzerEnglish(statue, many=True)
        return Response(serializer.data)


    
class CBV_StatuePredict(APIView):

    def get_object(self, id):
        try:
            return Statue.objects.filter(name=id)
        except ObjectDoesNotExist:
            raise Http404

    def get(self,request):
        try:
            img = request.FILES["image"]
            imageBinaryBytes = img.read()
            imageStream = io.BytesIO(imageBinaryBytes)
            imageFile = Image.open(imageStream)
            random_name = ''.join(random.choices(string.digits , k = 7))
            try:
                imageFile.save(random_name + ".jpg")
                img = cv2.imread(random_name + ".jpg")
                img2 = cv2.resize(img,[250,250])
                print(img2.shape)
                model = keras.models.load_model("ML models/VGG2.h5")
                pre1 = (model.predict(np.asarray([img2])))
                prob = pre1[0][np.argmax(pre1)]
                print(prob)
                print(classes_names[np.argmax(pre1)])
                if (prob>.99994) :
                    id = classes_names[np.argmax(pre1)]
                else :
                    id = "Unknown"
                original = random_name + ".jpg"
                target =id + original
                shutil.copyfile(original, target)
                os.remove(original)
            except:
                imageFile.save(random_name + ".png")
                img = cv2.imread(random_name + ".png")
                img2 = cv2.resize(img,[250,250])
                print(img2.shape)
                model = keras.models.load_model("ML models/VGG2.h5")
                pre1 = (model.predict(np.asarray([img2])))
                prob = pre1[0][np.argmax(pre1)]
                print(prob)
                print(classes_names[np.argmax(pre1)])
                if (prob>.99994) :
                    id = classes_names[np.argmax(pre1)]
                else :
                    id = "Unknown"
                original = random_name + ".png"
                target =id + original
                shutil.copyfile(original, target)
                os.remove(original)
            value = {
                "id": id,
            }
            id = value['id']
            statue = self.get_object(id)
            serializer = StatueSerialzerEnglish(statue, many=True)
            return Response(serializer.data)
        except:
            raise Http404
        

       












#Arabic views


class CBV_PlacesAr(APIView):
    permission_classes = (IsAuthenticated,)  
    def get(self,request):
        places = Place.objects.all()
        serializer = PlaceSerialzerArabic(places, many=True)
        return Response(serializer.data)

class CBV_Places_idAr(APIView):
    permission_classes = (IsAuthenticated,)  
    def get_object(self, id):
        try:
            return Place.objects.filter(id=id)
        except ObjectDoesNotExist:
            raise Http404

    def get(self,request,id):
        place = self.get_object(id)
        serializer = PlaceSerialzerArabic(place, many=True)
        return Response(serializer.data)

class CBV_StatuesAr(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        statues = Statue.objects.all()
        serializer = StatueSerialzerArabic(statues, many=True)
        return Response(serializer.data)

class CBV_Statues_idAr(APIView):
    permission_classes = (IsAuthenticated,)  
    def get_object(self, id):
        try:
            return Statue.objects.filter(id=id)
        except ObjectDoesNotExist:
            raise Http404

    def get(self,request,id):
        statue = self.get_object(id)
        serializer = StatueSerialzerArabic(statue, many=True)
        return Response(serializer.data)

class CBV_StatuePlaceAr(APIView):
    permission_classes = (IsAuthenticated,)  
    def get_object(self, place):
        try:
            place = self.kwargs['place']
            return Statue.objects.filter(place=place)
        except ObjectDoesNotExist:
            raise Http404

    def get(self,request,place):
        statue = self.get_object(place)
        serializer = StatueSerialzerArabic(statue, many=True)
        return Response(serializer.data)
