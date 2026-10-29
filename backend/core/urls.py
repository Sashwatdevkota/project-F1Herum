from django.urls import path
from .views import health_check, driver_standings

urlpatterns = [
    path("health/", health_check, name="health-check"),
    path("standings/", driver_standings, name="driver_standings "),
]