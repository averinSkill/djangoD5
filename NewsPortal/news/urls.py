from django.urls import path
from .views import NewsList, NewsDetail


urlpatterns = [
    # path('newsLLL/', index, name='index'),
    # path('new/<str:slug>', detail, name='detail'),
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view()),
    # path('news_list/', NewsList.as_view()),
]




