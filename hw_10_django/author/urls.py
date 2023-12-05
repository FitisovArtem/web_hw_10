from django.urls import path
from . import views

app_name = 'author'

urlpatterns = [
    path('<str:id_>', views.main, name='<str:id_>')
]
