# posts/urls.py
from django.urls import path
import posts.views
urlpatterns = [
    path('',posts.views.home, name='home'),
]
