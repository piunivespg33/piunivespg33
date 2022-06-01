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


class CSVSerializer(serializers.Serializer):
    autores = serializers.CharField(allow_blank=True, allow_null=True)
    titulo = serializers.CharField(allow_blank=True, allow_null=True)
    fonte_artigo = serializers.CharField(allow_blank=True, allow_null=True)
    palavras_chave = serializers.CharField(allow_blank=True, allow_null=True)
    resumo_artigo = serializers.CharField(allow_blank=True, allow_null=True)
    endereco_autores = serializers.CharField(allow_blank=True, allow_null=True)
    instituição_vinculo_autores = serializers.CharField(allow_blank=True, allow_null=True)
    agencia_fomento = serializers.CharField(allow_blank=True, allow_null=True)
    contagem_citacoes = serializers.CharField(allow_blank=True, allow_null=True)
    ano_publicacao = serializers.CharField(allow_blank=True, allow_null=True)
    areas_pesquisa = serializers.CharField(allow_blank=True, allow_null=True)
