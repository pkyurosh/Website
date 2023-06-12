from django.urls import path
from .views import homepageMsg,about,contact

urlpatterns = [
    path("home", view = homepageMsg, name="homepage"),
    path("about", view=about,name="about"),
    path("contact", view=contact, name="contact")
]
