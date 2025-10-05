from rest_framework import viewsets
from military.models import MilitaryBase
from military.serializers import MilitaryBaseModelSerializer

class MilitaryBaseModelViewSet(viewsets.ModelViewSet):
    queryset = MilitaryBase.objects.all()
    serializer_class = MilitaryBaseModelSerializer