from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from webnews.models import Newspaper, Redactor, Topic


def index(request):
    news_list = Newspaper.objects.all().select_related("topic")
    context = {
        "news_list": news_list,
    }
    return render(request, "webnews/index.html", context=context)


class NewspaperDetailView(generic.DetailView):
    model = Newspaper

