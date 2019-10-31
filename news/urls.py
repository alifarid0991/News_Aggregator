from . import api
from django.urls import path
urlpatterns = [
    path('news/',api.NewsList.as_view(),name="News Api"),
]
