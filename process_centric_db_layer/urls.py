from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from process_centric_db_layer import views
from travelando import settings

router = routers.SimpleRouter()

urlpatterns = [
    path('', include(router.urls)),
    path(r'save/', views.SaveProcessCentricDBView.as_view(), name='save'),
    path(r'retrieve/', views.RetrieveProcessCentricDBView.as_view(), name='retrieve'),
    path(r'delete/', views.DeleteProcessCentricDBView.as_view(), name='delete'),
]
