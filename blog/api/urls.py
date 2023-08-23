from django.urls import path, include
from .views import UserViewSet, PostViewSet, LikeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
