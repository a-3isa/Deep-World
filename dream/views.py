from .models import Dream
# from .serializers import DreamSerializer
from rest_framework.response import Response
import os 
from rest_framework import status
from rest_framework.views import APIView
import base64
import random
import urllib
from django.core.files.storage import FileSystemStorage
import requests
from PIL import Image
import base64
import io


fs = FileSystemStorage()
class Images(APIView):

    def post(self,request):

            myfile = request.FILES['image']
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            print(os.getcwd())
            style=request.POST.get("style")

            os.system(f'python test.py  {os.getcwd()}/{uploaded_file_url} {style}')
            ip=open('ip.txt','r').readline()
            return Response({"result": f"http://{ip}:599{uploaded_file_url}"}, status=status.HTTP_200_OK)


class Prism(APIView):

    def post(self,request):

            content = request.FILES['content']
            style = request.FILES['style']

            content = fs.save(content.name, content)
            style = fs.save(style.name, style)

            content_url = fs.url(content)
            style_url = fs.url(style)

            print(os.getcwd())
            os.system(f'python prism.py  {os.getcwd()}/{content_url} {os.getcwd()}/{style_url}')
            ip=open('ip.txt','r').readline()
            return Response({"result": f"http://{ip}:599{content_url}"}, status=status.HTTP_200_OK)
      





