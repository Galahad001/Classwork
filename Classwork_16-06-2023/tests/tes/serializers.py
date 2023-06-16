from rest_framework import serializers
from .models import *

class TestsSer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'