from rest_framework import serializers
from main.models import *
from .models import *


class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"
