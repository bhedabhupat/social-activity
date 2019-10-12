from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

app_name = 'core'
urlpatterns = [
    path('home', HomeView, name='home'),
]