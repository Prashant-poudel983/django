from django.urls import path
from . import views

urlpatterns = [
    path("detail", views.detail,name="detail"),
    path("", views.home,name="home")
]