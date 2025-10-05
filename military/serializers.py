from rest_framework import serializers
from military.models import MilitaryBase

class MilitaryBaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilitaryBase
        fields = '__all__'