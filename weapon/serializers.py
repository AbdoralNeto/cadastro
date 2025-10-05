from rest_framework import serializers
from weapon.models import Weapon

class WeaponModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = '__all__'