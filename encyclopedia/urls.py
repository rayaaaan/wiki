from django.urls import path

from . import views

app_name='q'

urlpatterns = [
    path("", views.index, name="index1"),
    path("wiki/<str:name>/",views.title, name="title"),
    path("search/", views.search, name="search"),
    path("add-page/", views.add_page, name="add_page"),
    path("RANDOM-PAGE/", views.random, name="random"),
    path("my-pages", views.my_pages,name="my_pages"),
]
