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
from .cleaner import word_dect
from .spam_dect import spam_dect

json_str = '{"Python": 150, "Java": 120, "JavaScript": 80, "Ruby": 40, "Go": 20}'
json_str = json.loads(json_str)
text = " ".join([k for k in json_str.keys() for i in range(json_str[k])])


# Create your views here.

@api_view(["GET", "POST"])
@csrf_exempt
def word_cloud(request):
    """
    Generate word cloud
    :param request: request from front-end
    :return: JSON to frontend
    """
    if request.method not in ["GET", "POST"]:
        """
        if request is nether GET nor POST, return error to front end.
        """
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    wordcloud = WordCloud(width=1920, height=1080, background_color="white", max_words=1000, contour_width=3,
                          contour_color='steelblue')
    if request.method == 'POST':
        """
        If request is Post, insert Json into database first.
        """
        json_data = json.loads(request.body)
        word = json_data.get('word')
        if not word_dect(word):
            return JsonResponse({'status': 'error', 'message': 'Invalid word input'})
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
@csrf_exempt
def get_year_data(request):
    """
    Get year_data for front end
    :param request: request from front-end
    :return: JSON to frontend
    """
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
def get_word_list(request):
    words = Word.objects.all().values('word')
    data = json.dumps(list(words))
    return HttpResponse(data, content_type='application/json')


@api_view(["GET"])
@csrf_exempt
def get_top_word(request):
    """
    Get the top 5 word in database
    :param request: request from front-end
    :return: JSON to frontend
    """
    top_words = Word.objects.order_by('-count')[:5]
    serializer = WordsSerializer(top_words, many=True)
    return Response(serializer.data)


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


@api_view(["GET"])
@csrf_exempt
def test(request, *args, **kwargs):
    wordcloud = WordCloud(width=1920, height=1080, background_color="#333", max_words=1000, contour_width=3,
                          contour_color='steelblue')
    result = generate_wordcloud_by_database(wordcloud)
    return HttpResponse(result, content_type='image/png')


@api_view(["POST"])
@csrf_exempt
def spam_detection(request, *args, **kwargs):
    input_text = request.data.get('text')  # request from front end
    if not input_text:
        return Response({'error': 'input_text field is required.'})
    result,result_num = spam_dect(input_text)
    return Response({'result': result, 'result_num': result_num}) # Return result to front_end

@api_view(['POST'])
@csrf_exempt
def password_evaluator(request, *args, **kwargs):
    input_password = request.data.get('text')
    if not input_password:
        return Response({'error':'text input require'})
    result_color,result_str = eval(text)
    return Response({'color':result_color,'result':result_str})