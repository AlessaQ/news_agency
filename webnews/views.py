from django.http import HttpResponse
from django.shortcuts import render
from webnews.models import Newspaper, Redactor, Topic


def index(request):
    num_newspaper = Newspaper.objects.count()
    num_redactors = Redactor.objects.count()
    num_topic = Topic.objects.count()
    # Показывает количество посещений страницы
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_newspaper": num_newspaper,
        "num_redactors": num_redactors,
        "num_topic": num_topic,
        "num_visits": num_visits,
    }
    return render(request, "webnews/index.html", context=context)
