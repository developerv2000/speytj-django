from django.urls import path

from mainapp import views


urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
]

