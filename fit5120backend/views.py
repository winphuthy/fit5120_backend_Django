import os
from django.http import HttpResponse
from fit5120Django import settings
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET", "POST"])
def word_cloud(request, *args, **kwargs):
    image_path = os.path.join(settings.BASE_DIR, 'fit5120backend', 'static', 'TestPicture.jpg')
    with open(image_path, 'rb') as f:
        image_data = f.read()
    return HttpResponse(image_data, content_type='image/png')