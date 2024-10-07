from django.shortcuts import render
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = "homepage.html"

class AboutMe(TemplateView):
    template_name = "aboutme.html"

class Portfolio(TemplateView):
    template_name = "portfolio.html"

class Blog(TemplateView):
    template_name = "blog.html"