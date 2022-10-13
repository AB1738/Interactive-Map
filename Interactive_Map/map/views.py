from django.shortcuts import render #noqa: F401
from django.http import HttpResponse #noqa: F401
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class Mapview(TemplateView):
    template_name = "map.html"
