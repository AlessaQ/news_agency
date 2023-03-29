from django.urls import path

from webnews.views import index

urlpatterns = [
    path("", index),
]
app_name = "webnews"
