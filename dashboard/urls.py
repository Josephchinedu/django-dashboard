from django.urls import path
from .views import *

urlpatterns = [
    path('', dash_board)
]
