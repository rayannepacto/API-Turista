from rest_framework.viewsets import ModelViewSet
from atracoes.models import Local
from .serializers import AtracaoSerializer


class AtracaoViewSet(ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = AtracaoSerializer
