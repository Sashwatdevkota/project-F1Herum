from django.urls import path
from .views import *

urlpatterns = [
    path("health/", health_check, name="health-check"),
    path("standings/", driver_standings, name="driver_standings "),
    path("first-driver/", first_driver_name, name="first-driver"),
]