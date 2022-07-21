from contextvars import Token
import io
import os
from unicodedata import name
import cv2
import  keras
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse
from numpy import place
from PIL import Image
from PIL import Image, ExifTags
from matplotlib import image
from matplotlib.font_manager import json_dump
import numpy as np
from .serializers import  PlaceSerialzer, StatueSerialzer
from .models import Statue, Place
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import TokenAuthentication   



classes_names = ['Amenhotep, Son of Hapu', 'Amenophis III his wife', 'Egyptian Writer', 'Hatshepsut', 'I Senwosert', 'III Senwosret', 'III Sphinxes of Amenemhat', 'Isis, mother of king Thutmose III', 'Khafre', 'Menkaure, Hathor and the gods', 'Narmer painting face 1', 'Narmer painting face 2', 'no name', 'Nofert', 'Pyramid', 'Rahotep', 'Rahotep and Nofret', 'Ramesses II usurped by Merenptah', 'Ramses II as a Standard Bearer', 'Sphinx']
modeldir = os.listdir("ML models")
listofmodels = []
for mod in modeldir:
    model = keras.models.load_model("ML models/"+mod)
    listofmodels.append(model)

#English Views

class CBV_Places(APIView):
    permission_classes = (IsAuthenticated,)  
    def get(self,request):
        places = Place.objects.all()
        serializer = PlaceSerialzer(places, many=True)
        return Response(serializer.data)

class CBV_Places_id(APIView):
    permission_classes = (IsAuthenticated,)  
    def get_object(self, id):
        try:
            return Place.objects.filter(id=id)
        except ObjectDoesNotExist:
            raise Http404

    def get(self,request,id):
        place = self.get_object(id)
        serializer = PlaceSerialzer(place, many=True)
        return Response(serializer.data)

class CBV_Statues(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        statues = Statue.objects.all()
        serializer = StatueSerialzer(statues, many=True)
        return Response(serializer.data)

class CBV_Statues_id(APIView):
    permission_classes = (IsAuthenticated,)  
    def get_object(self, id):
        try:
            return Statue.objects.filter(id=id)
        except ObjectDoesNotExist:
            raise Http404

    def get(self,request,id):
        statue = self.get_object(id)
        serializer = StatueSerialzer(statue, many=True)
        return Response(serializer.data)

class CBV_StatuePlace(APIView):
    permission_classes = (IsAuthenticated,)  
    def get_object(self, place):
        try:
            return Statue.objects.filter(place=place)
        except ObjectDoesNotExist:
            raise Http404

    def get(self,request,place):
        statue = self.get_object(place)
        serializer = StatueSerialzer(statue, many=True)
        return Response(serializer.data)


    
class CBV_StatuePredict(APIView):

    def get_object(self, result , place):
        try:
            return Statue.objects.filter(name=result,place_id=place)
        except ObjectDoesNotExist:
            raise Http404

    def post(self,request,place):
        try:
            img = request.FILES["image"]
            imageBinaryBytes = img.read()
            imageStream = io.BytesIO(imageBinaryBytes)
            imageFile = Image.open(imageStream)
            model = listofmodels[int(place)-1]
            try:
                for orientation in ExifTags.TAGS.keys():
                        if ExifTags.TAGS[orientation]=='Orientation':
                            break
                exif = imageFile._getexif()

                if exif[orientation] == 3:
                    imageFile=imageFile.rotate(180, expand=True)
                elif exif[orientation] == 6:
                    imageFile=imageFile.rotate(270, expand=True)
                elif exif[orientation] == 8:
                    imageFile=imageFile.rotate(90, expand=True)
            except:
                pass
            try:                
                imageFile.save("pre.jpg")
                imageFile.close()
                img = cv2.imread("pre.jpg")
                img2 = cv2.resize(img,[250,250])
                pre1 = (model.predict(np.asarray([img2])))
                prob = pre1[0][np.argmax(pre1)]
                print(prob)
                print(classes_names[np.argmax(pre1)])
                if (prob>0.9999999999) :
                    result = classes_names[np.argmax(pre1)]
                else :
                    result = "Unknown"
            except:
                imageFile.save("pre.png")
                imageFile.close()
                img = cv2.imread("pre.png")
                img2 = cv2.resize(img,[250,250])
                pre1 = (model.predict(np.asarray([img2])))
                prob = pre1[0][np.argmax(pre1)]
                print(prob)
                print(classes_names[np.argmax(pre1)])
                if (prob>0.9999999999) :
                    result = classes_names[np.argmax(pre1)]
                else :
                    result = "Unknown"          
            value = {
                "result": result,
            }
            result = value['result']
            statue = self.get_object(result,place)
            serializer = StatueSerialzer(statue, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            raise Http404