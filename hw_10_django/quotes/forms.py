import datetime

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField, TextInput, DateField, DateInput, ChoiceField, ModelForm, ModelChoiceField
from . import models


class CreateAuthorForm(UserCreationForm):
    fullname = CharField(max_length=60, min_length=3, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    born_date = DateField(required=True, widget=DateInput(attrs={'class': 'form-control'}))
    born_location = CharField(max_length=60, min_length=3, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    description = CharField(required=True, widget=TextInput(attrs={'class': 'form-control'}))
    # created_at = datetime.datetime.now()

    class Meta:
        model = User
        fields = ('fullname', 'born_date', 'born_location', 'description')


class CreateQuoteForm(UserCreationForm):
    quote = CharField(max_length=60, min_length=3, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    # created_at = datetime.datetime.now()
    author_id = CharField(required=True, widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('quote', 'author_id')
