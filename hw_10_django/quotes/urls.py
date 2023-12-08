from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('createAuthor', views.RegisterAuthorView, name='createAuthor'),
    path('createQuote', views.RegisterQuoteView, name='createQuote'),
    path('createTag', views.RegisterTagView, name='createTag'),
    path('tag/<str:t_name>', views.find_tags, name='find_tags'),
    path('scraping', views.scraping, name='scraping'),
]
