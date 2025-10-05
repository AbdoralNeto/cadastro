from django.urls import path, include
from rest_framework.routers import DefaultRouter
from weapon.views import WeaponModelViewSet

router = DefaultRouter()
router.register('weapons', WeaponModelViewSet)
urlpatterns = [
    path('', include(router.urls)),
]