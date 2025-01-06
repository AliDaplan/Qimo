from django.urls import path
from . import views

app_name="MENU"

urlpatterns = [
    path("", views.index, name="index"),
]
