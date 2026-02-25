from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("marilyn", views.marilyn, name="marilyn"),
    path("webgemini", views.webgemini, name="webgemini"),
    path("<str:name>", views.greet, name="greet"),
]
