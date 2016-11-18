from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required


def hello_world(request):
    return HttpResponse('hello world')
