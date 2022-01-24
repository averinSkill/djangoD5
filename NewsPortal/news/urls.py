from django.urls import path
from .views import NewsList, NewsDetail, Search, NewsAdd, NewsEdit, NewsDelete


urlpatterns = [
    # path('newsLLL/', index, name='index'),
    # path('new/<str:slug>', detail, name='detail'),
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
    # path('<int:pk>', NewsDetailView.as_view()),
    path('search/', Search.as_view(), name='search'),
    path('add/', NewsAdd.as_view(), name='news_create'),
    path('edit/<int:pk>', NewsEdit.as_view(), name='news_edit'),
    path('delete/<int:pk>', NewsDelete.as_view(), name='news_delete'),

]




