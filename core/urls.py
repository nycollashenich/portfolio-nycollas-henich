from django.urls import path
from .views import *

urlpatterns = [
    path('nycollashenich/', IndexView.as_view(), name='index'),
]
