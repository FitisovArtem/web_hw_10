from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .utils import get_mongodb
from .forms import CreateAuthorForm, CreateQuoteForm


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page=per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


class RegisterAuthorView(View):
    template_name = 'quotes/registerAuthor.html'
    form_class = CreateAuthorForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            fullname = form.cleaned_data['fullname', 'born_date', 'born_location', 'description']
            messages.success(request, f'New author: {fullname} created')
            return redirect(to='/')
        return render(request, self.template_name, {'form': form})


class RegisterQuoteView(View):
    template_name = 'quotes/registerQuote.html'
    form_class = CreateQuoteForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            fullname = form.cleaned_data['fullname']
            messages.success(request, f'New Quote created')
            return redirect(to='/')
        return render(request, self.template_name, {'form': form})

