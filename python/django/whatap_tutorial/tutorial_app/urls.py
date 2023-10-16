from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("health_check/", views.health_check, name="health_check"),
    path("error_check/", views.error_check, name="error_check")
]
