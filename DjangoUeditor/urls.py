# coding:utf-8
from django import VERSION
from django.conf.urls import url

from .views import get_ueditor_controller
from .widgets import UEditorWidget, AdminUEditorWidget

urlpatterns = [
    url(r'^controller/$', get_ueditor_controller),
]
