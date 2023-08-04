from django.shortcuts import render
from django.http import HttpResponse
from .models import NoinfoDetail
from django.template import loader

def index(request):
    text = NoinfoDetail.objects.all()
    context = {
        "text": text,
    }
    return render(request, "noinfo/index.html", context)