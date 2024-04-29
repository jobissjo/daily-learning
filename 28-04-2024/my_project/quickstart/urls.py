# quickstart/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router
router = DefaultRouter()

# Register viewsets with the router
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Include the router URLs directly
urlpatterns = [
    path('', include(router.urls)),
]
