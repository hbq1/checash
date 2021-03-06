# coding: utf-8

from django.conf.urls import url, include
from rest_framework import routers

from .views import PersonViewSet


router = routers.DefaultRouter()

router.register('user', PersonViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
