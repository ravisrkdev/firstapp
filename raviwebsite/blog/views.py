import imp
from django.shortcuts import render
from blog.models import Banner
# Create your views here.
from django.http import HttpResponse


def homepage(request):
    title_and_subtitle = Banner.objects.get(id=1)
    return render(request, "templates/index.html", {'record': title_and_subtitle})