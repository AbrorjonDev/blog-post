from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class YouTubePageView(TemplateView):
    template_name = 'youtube.html'

class MyResumePageView(TemplateView):
    template_name = 'resume.html'

class AboutMeEngView(TemplateView):
    template_name = 'about-eng.html'