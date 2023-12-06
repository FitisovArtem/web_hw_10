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
    # result = models.Quote.objects.raw('select tag_id from quotes_quote_tags as q left join quotes_tag as tag on tag.id = q.tag_id group by q.tag_id order by count(*) desc')
    tags = models.Tag.objects.all().values()
    top_t = models.Quote.tags.through.objects.all().values('tag_id', 'tag').annotate(total=Count('tag_id')).order_by('-total')[:10]
    top_tags = []
    for tag in top_t:
        print(tag)
        for t in tags:
            if tag['tag_id'] == t['id']:
                top_tags.append([t['name'], tag['total']])
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
    tags = models.Tag.objects.all().values()
    top_t = models.Quote.tags.through.objects.all().values('tag_id', 'tag').annotate(total=Count('tag_id')).order_by(
        '-total')[:10]
    top_tags = []
    for tag in top_t:
        print(tag)
        for t in tags:
            if tag['tag_id'] == t['id']:
                top_tags.append([t['name'], tag['total']])
    return render(request, 'quotes/index.html', context={'quotes': page_object, 'top_tags': top_tags})

