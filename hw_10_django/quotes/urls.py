from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('createAuthor', views.RegisterAuthorView.as_view(), name='createAuthor'),
    path('createQuote', views.RegisterQuoteView.as_view(), name='createQuote'),
]
