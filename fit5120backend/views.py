import os
import json
from rest_framework import serializers
from .serializers import YearDataSerializer
from django.http import HttpResponse, JsonResponse
from fit5120Django import settings
from fit5120backend.models import Yeardata
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(["GET", "POST"])
def word_cloud(request, *args, **kwargs):
    image_path = os.path.join(settings.BASE_DIR, 'fit5120backend', 'static', 'TestPicture.jpg')
    with open(image_path, 'rb') as f:
        image_data = f.read()
    return HttpResponse(image_data, content_type='image/png')


@api_view(["GET"])
def get_year_data(request, *args, **kwargs):
    try:
        year_data = Yeardata.objects.all()
        serializer = YearDataSerializer(year_data, many=True)
        return Response(serializer.data)
    except serializers.ValidationError as e:
        return JsonResponse({'msg': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'msg': 'Server Error'}, status=500)


@api_view(["GET"])
def test(request, *args, **kwargs):
    try:
        year_data = Yeardata.objects.all()
        serializer = YearDataSerializer(year_data, many=True)
        json_data = json.loads(json.dumps(serializer.data))
        return JsonResponse(json_data, safe=False, content_type='application/json')
    except serializers.ValidationError as e:
        return JsonResponse({'msg': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'msg': 'Server Error'}, status=500)
