from django.shortcuts import render, get_object_or_404
from .models import News
from datetime import datetime

def news_list(request):
    news = News.objects.all().order_by('-create_time')
    return render(request, 'News.html', {'news': news})


def news_detail(request, id):
    news_item = get_object_or_404(News, id=id)
    return render(request, 'News_detail.html', {'news': news_item})
