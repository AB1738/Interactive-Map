from django.urls import path
from .views import HomePageView, Mapview

urlpatterns = [
path('', HomePageView.as_view(), name='home'),
path('map/', Mapview.as_view(), name='map'),
]