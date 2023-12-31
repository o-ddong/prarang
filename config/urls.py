"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from applications.places.views import PlaceViewSet
from applications.translates.views import GoogleTranslateViewSet, ChatGPTAPIView

router = SimpleRouter(trailing_slash=False)

router.register('v1', PlaceViewSet, 'places')
router.register('v1/google', GoogleTranslateViewSet, 'google')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    path('v1/chatgpt', ChatGPTAPIView.as_view()),
]
