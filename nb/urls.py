

from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('update', index_update),
]
