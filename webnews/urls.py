from django.urls import path

from webnews.views import index, NewspaperDetailView

urlpatterns = [
    path("123/", index),
    path(
        "newspaper/<int:pk>/",
        NewspaperDetailView.as_view(),
        name="newspaper-detail"
    ),
]
app_name = "webnews"

