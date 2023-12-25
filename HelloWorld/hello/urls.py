from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("<str:name>", views.sasa, name = "sasa"),
    path("Dan", views.Dan, name="Dan"),
    #path("<str:name>", views.greet, name = "greet")
]
