from rest_framework import serializers
from .models import Dream

class DreamSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,allow_empty_file=False, use_url=True,)
    style=serializers.CharField(max_length=None,allow_blank=False)
    class Meta:
        model = Dream
        fields = ['style','image']





