from django.urls import path

from webnews.views import (
    index,
    NewspaperDetailView,
    RedactorListView,
)

urlpatterns = [
    path("123/", index),
    path(
        "newspaper/<int:pk>/",
        NewspaperDetailView.as_view(),
        name="newspaper-detail"
    ),
    path(
        "redactors/",
        RedactorListView.as_view(),
        name="redactor-list"
    ),
]
app_name = "webnews"

