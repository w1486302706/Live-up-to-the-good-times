from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import NoinfoDetail
from .forms import DetailForm

# 主页面
def index(request):
    # 获取NoinfoDetail全部数据
    text = NoinfoDetail.objects.all()
    context = {
        "text": text,
    }
    return render(request, "noinfo/index.html", context)

# 明细页面
def detail(request):
    # 获取NoinfoDetail全部数据
    text = NoinfoDetail.objects.all()
    context = {
        "text": text,
    }
    return render(request, "noinfo/detail.html", context)

def submit_detail_form(request):
    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('/success/')
    else:
        form = DetailForm()
    return render(request, 'noinfo/submit_detail_form.html', {'form': form})