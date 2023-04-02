from django.http import HttpResponse
from django.shortcuts import render
from webnews.models import Newspaper, Redactor, Topic


def index(request):
    news_list = Newspaper.objects.all().select_related("topic")
    context = {
        "news_list": news_list,
    }
    return render(request, "webnews/index.html", context=context)
