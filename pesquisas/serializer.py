from rest_framework import serializers

from pesquisas.models import Pesquisa


class PesquisaFiltrosSerializer(serializers.Serializer):

    campo = serializers.CharField(required=True)
    valor = serializers.CharField(required=True)
    tipo = serializers.ChoiceField(choices=["istartswith", "iendswith", "contains"])


class PesquisaSerializar(serializers.ModelSerializer):

    class Meta:
        model = Pesquisa
        fields = '__all__'
