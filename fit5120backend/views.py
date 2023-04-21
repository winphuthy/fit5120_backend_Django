import json
from io import BytesIO

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from wordcloud import WordCloud

from .models import Word
from .models import Yeardata
from .serializers import YearDataSerializer, WordsSerializer

json_str = '{"Python": 150, "Java": 120, "JavaScript": 80, "Ruby": 40, "Go": 20}'
json_str = json.loads(json_str)
text = " ".join([k for k in json_str.keys() for i in range(json_str[k])])


# Create your views here.

@api_view(["GET", "POST"])
def word_cloud(request, *args, **kwargs):
    if request.method not in ["GET", "POST"]:
        """
        if request is nether GET nor POST, return error to front end.
        """
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    wordcloud = WordCloud(background_color="white", max_words=1000, contour_width=3, contour_color='steelblue')
    if request.method == 'POST':
        """
        If request is Post, insert Json into database first.
        """
        json_data = json.loads(request.body)
        word = json_data.get('word')
        if not word:
            return JsonResponse({'status': 'error', 'message': 'Missing word'})
        try:
            word_obj = Word.objects.get(word=word)
            word_obj.increment_count()
        except Word.DoesNotExist:
            word_obj = Word(word=word, count=1)
            word_obj.save()
    """
    if request in GET or Post, Generate wordcloud from database and send back to front end.
    """
    result = generate_wordcloud_by_database(wordcloud)
    return HttpResponse(result, content_type='image/png')


@api_view(["GET"])
def get_year_data(request, *args, **kwargs):
    try:
        year_data = Yeardata.objects.all()
        serializer = YearDataSerializer(year_data, many=True)
        return Response(serializer.data)
    except serializers.ValidationError as e:
        return JsonResponse({'msg': str(e)}, status=400)
    except Exception:
        return JsonResponse({'msg': 'Server Error'}, status=500)


@api_view(["GET"])
@csrf_exempt
def test(request, *args, **kwargs):
    wordcloud = WordCloud(background_color="white", max_words=1000, contour_width=3, contour_color='steelblue')
    result = generate_wordcloud_by_database(wordcloud)
    return HttpResponse(result, content_type='image/png')


def generate_wordcloud_by_database(wordcloud):
    """
    Generate wordcloud from database
    :param wordcloud: wordcloud has been identified
    :return: wordcloud picture in byt
    """
    words = Word.objects.all()
    serializer = WordsSerializer(words, many=True)
    # print(serializer.data)
    # return Response(serializer.data)
    reformat = {}
    for item in serializer.data:
        reformat[item['word']] = item['count']
    image = wordcloud.generate_from_frequencies(reformat)
    result = wordCloudImg_to_byt(image)
    return result


def wordCloudImg_to_byt(image):
    """
    Transfer wordCloud image class to byt data
    :param image: wordCloud class image
    :return:the byt class picture
    """
    img_bytes = BytesIO()
    image.to_image().save(img_bytes, format='PNG')
    result = img_bytes.getvalue()
    return result
