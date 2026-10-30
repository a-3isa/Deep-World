from .models import Dream
# from .serializers import DreamSerializer
from rest_framework.response import Response
import os 
import re
import subprocess
import sys
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

# A style names a model file, models/<style>.pb: letters, digits, - and _ only.
STYLE_NAME = re.compile(r"[A-Za-z0-9_-]{1,64}")


def run_script(*args):
    # Arguments go straight to the interpreter, never through a shell, so
    # nothing in them can run as a command.
    subprocess.run([sys.executable, *args], check=False)

class Images(APIView):

    def post(self,request):

            myfile = request.FILES['image']
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            print(os.getcwd())
            style=request.POST.get("style")
            if not style or not STYLE_NAME.fullmatch(style):
                return Response({"style": "Use a model name: letters, digits, - and _."}, status=status.HTTP_400_BAD_REQUEST)

            run_script('test.py', f'{os.getcwd()}/{uploaded_file_url}', style)
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
            run_script('prism.py', f'{os.getcwd()}/{content_url}', f'{os.getcwd()}/{style_url}')
            ip=open('ip.txt','r').readline()
            return Response({"result": f"http://{ip}:599{content_url}"}, status=status.HTTP_200_OK)
      





