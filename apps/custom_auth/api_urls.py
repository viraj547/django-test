from rest_framework.routers import DefaultRouter
from .api import LoginViewSet
from django.urls import path, include

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('login/',LoginViewSet.as_view(),name='login')
]
