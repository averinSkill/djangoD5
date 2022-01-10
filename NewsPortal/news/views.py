from datetime import datetime
from django.views.generic import ListView, DetailView
from news.models import Post, Author
from django.http import HttpResponse
from django.shortcuts import render


class NewsList(ListView):
    model = Post
    context_object_name = 'news_list'
    template_name = 'news/news.html'
    # context_object_name = 'news_list'
    # template_name = 'news/news_list.html'
    queryset = Post.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        return context

class NewsDetail(DetailView):
    model = Post
    context_object_name = 'news_detail'
    template_name = 'news/news_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        return context


