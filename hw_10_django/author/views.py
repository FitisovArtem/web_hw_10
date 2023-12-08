from bson.objectid import ObjectId
from django.shortcuts import render
from .utils import get_mongodb


def main(request, id_):
    db = get_mongodb()
    authors = db.authors.find_one({'fullname': id_})
    return render(request, 'author/index.html', context={'authors': authors})
