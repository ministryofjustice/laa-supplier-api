# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view


router = routers.DefaultRouter(trailing_slash=False)

schema_view = get_swagger_view(title='Calculator API')

urlpatterns = (
    url(r'^', include(router.urls)),
    url(r'^docs$', schema_view)
)
