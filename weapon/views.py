from rest_framework import viewsets
from weapon.models import Weapon
from weapon.serializers import WeaponModelSerializer

class WeaponModelViewSet(viewsets.ModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponModelSerializer
