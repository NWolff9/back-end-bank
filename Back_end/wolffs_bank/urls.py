from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from cadastro.api.viewsets import ClienteViewSet

route = routers.DefaultRouter()
route.register(r'cliente', ClienteViewSet, basename="Cliente")

urlpatterns = [
     path('', include(route.urls)),
     path('admin/', admin.site.urls),
]
