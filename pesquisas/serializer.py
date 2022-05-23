from email.policy import default
from rest_framework import serializers

from pesquisas.models import Pesquisa


class PesquisaFiltrosSerializer(serializers.Serializer):

    campo = serializers.CharField(required=True)
    valor = serializers.CharField(required=True)
    tipo = serializers.ChoiceField(
        choices=["istartswith", "iendswith", "contains"]
    )


class PesquisaPaginacaoSerializer(serializers.Serializer):
    pagina = serializers.IntegerField(required=False, default=1)
    quantidade = serializers.IntegerField(required=False, default=25)
    filtros = PesquisaFiltrosSerializer(many=True, required=False, default=[])


class PesquisaSerializar(serializers.ModelSerializer):

    class Meta:
        model = Pesquisa
        fields = '__all__'
