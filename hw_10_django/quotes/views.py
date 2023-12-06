from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, redirect
from . import models

from .utils import get_mongodb
from .forms import CreateAuthorForm, CreateQuoteForm, CreateTagForm


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page=per_page)
    quotes_on_page = paginator.page(page)
    top_t = models.Quote.objects.values('tags__name', "tags__id") \
                   .annotate(quote_count=Count('tags__name')) \
                   .order_by('-quote_count')[:10]
    top_tags = []
    for tag in top_t:
        top_tags.append(tag['tags__name'])
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page, 'top_tags': top_tags})


def RegisterAuthorView(request):
    template_name = 'quotes/registerAuthor.html'
    form_class = CreateAuthorForm

    if request.method == 'POST':
        form = CreateAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='/')
        else:
            return render(request, template_name, context={'form': form_class})
    return render(request, template_name, context={'form': form_class})


def RegisterQuoteView(request):
    template_name = 'quotes/registerQuote.html'
    form_class = CreateQuoteForm

    if request.method == 'POST':
        form = CreateQuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='/')
        else:
            return render(request, template_name, context={'form': form_class})
    return render(request, template_name, context={'form': form_class})


def RegisterTagView(request):
    template_name = 'quotes/registerTag.html'
    form_class = CreateTagForm

    if request.method == 'POST':
        form = CreateTagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='/')
        else:
            return render(request, template_name, context={'form': form_class})
    return render(request, template_name, context={'form': form_class})


def find_tags(request, t_name):
    per_page = 10
    db = get_mongodb()
    quotes = db.quotes.find({
        "tags": {"$eq": t_name}})
    paginator = Paginator(list(quotes), per_page=per_page)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    top_t = models.Quote.objects.values('tags__name', "tags__id") \
                .annotate(quote_count=Count('tags__name')) \
                .order_by('-quote_count')[:10]
    top_tags = []
    for tag in top_t:
        top_tags.append(tag['tags__name'])
    return render(request, 'quotes/index.html', context={'quotes': page_object, 'top_tags': top_tags})

