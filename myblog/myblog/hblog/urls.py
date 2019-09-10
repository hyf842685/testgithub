from django.urls import path

from hblog import api
from .views import index

urlpatterns = [
    path('api/index', api.index),
    path('', index),
]
