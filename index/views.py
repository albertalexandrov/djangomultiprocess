import random
import time

from django.http import HttpResponse


def index(request):
    time.sleep(random.randint(0, 10))
    return HttpResponse('ok')
