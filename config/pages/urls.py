
from typing import Annotated, overload
from django.urls import path
from .views import  HomePageView,AboutPageView,YouTubePageView,MyResumePageView,AboutMeEngView

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('youtube/',YouTubePageView.as_view(),name='youtube'),
    path('my-resume/',MyResumePageView.as_view(),name='resume'),
    path('about-eng/',AboutMeEngView.as_view(),name='about-eng'),
]
