from django.urls import path

from . import views

app_name='q'

urlpatterns = [
    path("", views.index, name="index1"),
    path("wiki/<str:name>/",views.title, name="title"),
    path("search/", views.search, name="search"),
]
