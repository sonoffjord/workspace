# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BoardViewSet


router = DefaultRouter()
router.register(r'boards', BoardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
