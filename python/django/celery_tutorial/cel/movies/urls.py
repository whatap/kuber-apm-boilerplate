from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('test/', views.test, name="test"),

    path('sleep_test/', views.sleep_test, name="sleep_test"),

#    path('health_check/', views.health_check, name="health_check"),
#    path('active_stack_check/', views.active_stack_check, name="active_stack_check"),
#    path('error_check/', views.error_check, name="error_check")
]

