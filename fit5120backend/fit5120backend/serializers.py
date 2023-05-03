from rest_framework import serializers
from .models import Yeardata
from .models import Word

class YearDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yeardata
        fields = '__all__'

class WordsSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()
    class Meta:
        model = Word
        fields = [
            "word",
            "count"
        ]