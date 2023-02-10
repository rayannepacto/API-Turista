from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from endereco.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(serializers.ModelSerializer):
    local = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = [
            'nome', 'id', 'descricao', 'aprovado', 'foto',
            'local', 'comentarios', 'avaliacoes', 'endereco', 'descricao_completa'

        ]

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
