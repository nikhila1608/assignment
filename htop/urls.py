from django.urls import path
from . import views

urlpatterns = [
    path('', views.htop, name='htop'),  # This maps the root URL of the htop app
]
