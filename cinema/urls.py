from django.urls import path

from cinema import views as vv
from . import views

urlpatterns = [
    path('index/', vv.index),
    path('list/',vv.list),
    path('json/',vv.readerData)
]
