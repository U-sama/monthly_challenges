from django.urls import path
from . import views

urlpatterns = [
    path("", views.challenge_home, name='index'), # /challenges/
    path("<int:month>", views.monthly_challenge_num),
    path('<str:month>', views.monthly_challenge, name="month-challenge"),
   ]
