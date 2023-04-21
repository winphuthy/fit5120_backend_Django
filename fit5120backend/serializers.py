from rest_framework import serializers
from .models import Yeardata

class YearDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yeardata
        fields = '__all__'