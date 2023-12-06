from django.forms import CharField, TextInput, SelectMultiple, Select, ModelForm, ModelChoiceField, ModelMultipleChoiceField
from . import models


class CreateAuthorForm(ModelForm):
    fullname = CharField(max_length=50, min_length=3, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    born_date = CharField(max_length=50, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    born_location = CharField(max_length=150, min_length=3, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    description = CharField(max_length=50000, required=True, widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class CreateQuoteForm(ModelForm):
    quote = CharField(max_length=60, min_length=3, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    tags = ModelMultipleChoiceField(queryset=models.Tag.objects.all().order_by('name'), required=True,
                                    widget=SelectMultiple(attrs={'class': 'form-control'}))
    author = ModelChoiceField(queryset=models.Author.objects.all().order_by('fullname'),
                                 widget=Select(attrs={'class': 'form-control'}))

    class Meta:
        model = models.Quote
        fields = ['quote', 'tags', 'author']


class CreateTagForm(ModelForm):
    name = CharField(max_length=30, min_length=3, required=True, widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.Tag
        fields = ['name']
