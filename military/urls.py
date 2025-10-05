from django.urls import path, include
from rest_framework.routers import DefaultRouter
from military.views import MilitaryBaseModelViewSet

router = DefaultRouter()
router.register('bases', MilitaryBaseModelViewSet)
urlpatterns = [
    path('', include(router.urls)),
]