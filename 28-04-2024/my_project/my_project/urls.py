"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# main urls.py

from django.contrib import admin
from django.urls import path, include
from quickstart import urls as quickstart_urls
from posts import urls as post_urls

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', include(post_urls)),  
    path('snippets/', include('snippets.urls')),
    path('auth', include(quickstart_urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


