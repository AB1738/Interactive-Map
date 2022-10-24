from django.urls import path
from .views import HomePageView, MapView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("map/", MapView.as_view(), name="map"),
]
