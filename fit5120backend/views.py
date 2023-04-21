import os
import json
from rest_framework import serializers
from wordcloud import WordCloud
from io import BytesIO
from .serializers import YearDataSerializer
from django.http import HttpResponse, JsonResponse
from fit5120Django import settings
from fit5120backend.models import Yeardata
from rest_framework.decorators import api_view
from rest_framework.response import Response

json_str = '{"Python": 150, "Java": 120, "JavaScript": 80, "Ruby": 40, "Go": 20}'
json_str = json.loads(json_str)
text = " ".join([k for k in json_str.keys() for i in range(json_str[k])])


# Create your views here.

@api_view(["GET", "POST"])
def word_cloud(request, *args, **kwargs):
    if request.method == "GET":
        wordcloud = WordCloud(background_color="white", max_words=1000, contour_width=3, contour_color='steelblue')
        image = wordcloud.generate_from_frequencies(json_str)
        result = wordcloudimg_to_byt(image)
        return HttpResponse(result, content_type='image/png')
    if request.method == "POST":

        image_path = os.path.join(settings.BASE_DIR, 'fit5120backend', 'static', 'TestPicture.jpg')
        with open(image_path, 'rb') as f:
            image_data = f.read()
        return HttpResponse(image_data, content_type='image/png')
    else:
        return JsonResponse({'msg': "Wrong request type"}, status=400)


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
    wordcloud = WordCloud(background_color="white", max_words=1000, contour_width=3, contour_color='steelblue')
    image = wordcloud.generate_from_frequencies(json_str)
    result = wordcloudimg_to_byt(image)
    return HttpResponse(result, content_type='image/png')

def wordcloudimg_to_byt(image):
    """
    Transfer wordCloud image class to byt data
    :param image: wordCloud class image
    :return:the byt class picture
    """
    img_bytes = BytesIO()
    image.to_image().save(img_bytes, format='PNG')
    result = img_bytes.getvalue()
    return result
