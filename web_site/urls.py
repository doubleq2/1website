from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = 'home' ),
    path("about/", views.about, name = 'about'),
    path("photo/", views.photo, name = 'photo'),
    path("geography/", views.geography, name = 'geo'),
    path("papers/", views.papers, name = 'papers'),
    path("thanks/", views.thanks, name = 'thx'),
    path("people/", views.people, name = 'people')
]