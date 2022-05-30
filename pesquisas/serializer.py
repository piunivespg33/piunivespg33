from rest_framework import serializers
from django.core.validators import FileExtensionValidator

from pesquisas.models import Pesquisa


class PesquisaFiltrosSerializer(serializers.Serializer):

    campo = serializers.CharField(required=True)
    valor = serializers.CharField(required=True)
    tipo = serializers.ChoiceField(choices=["istartswith", "iendswith", "icontains"])


class PesquisaPaginacaoSerializer(serializers.Serializer):
    pagina = serializers.IntegerField(required=False, default=1)
    quantidade = serializers.IntegerField(required=False, default=25)
    filtros = PesquisaFiltrosSerializer(many=True, required=False, default=[])


class PesquisaSerializar(serializers.ModelSerializer):
    class Meta:
        model = Pesquisa
        exclude = ["user"]


class UploadSerializer(serializers.Serializer):

    file_uploaded = serializers.FileField()

    class Meta:
        fields = ["file_uploaded"]
