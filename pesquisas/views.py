import base64
import csv
import io

from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from pesquisas.models import Pesquisa
from pesquisas.serializer import (
    CSVSerializer,
    PesquisaPaginacaoSerializer,
    PesquisaSerializar,
)

from pesquisas.services import filtrar_pesquisas


def save_data(data, request):
    """
    Salva os dados no banco.
    """
    aux = []
    for item in data:
        # Atribui valor da coluna ao objeto
        autores = item.get("Autores")
        titulo = item.get("Título")
        fonte_artigo = item.get("Fonte do artigo")
        palavras_chave = item.get("Palavras-chave")
        resumo_artigo = item.get("Resumo do artigo")
        endereco_autores = item.get("Endereço dos Autores")
        instituição_vinculo_autores = item.get("Instituição de vínculo dos autores")
        agencia_fomento = item.get("Agência de Fomento")
        contagem_citacoes = item.get("Contagem do número de citações")
        ano_publicacao = item.get("Ano da publicação")
        areas_pesquisa = item.get("Áreas de pesquisa")
        obj = Pesquisa(
            # Carrega os valores do objeto para objeto da classe pesquisa
            autores=autores,
            titulo=titulo,
            fonte_artigo=fonte_artigo,
            palavras_chave=palavras_chave,
            resumo_artigo=resumo_artigo,
            endereco_autores=endereco_autores,
            instituição_vinculo_autores=instituição_vinculo_autores,
            agencia_fomento=agencia_fomento,
            contagem_citacoes=contagem_citacoes,
            ano_publicacao=ano_publicacao,
            areas_pesquisa=areas_pesquisa,
            user_id=request.user.id,
        )
        aux.append(obj)
    Pesquisa.objects.bulk_create(aux)

class CarregaPesquisaApi(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CSVSerializer(data=request.data)

        if serializer.is_valid():
            # Gerando uma list comprehension
            try:
                dados = serializer.data
                dados["user_id"] = request.user.id
                registro = Pesquisa(**dados)
                registro.save()

                return Response({}, status=status.HTTP_201_CREATED)
            except Exception as e:
                print(e)
                return Response(
                    {"erro": "Erro ao salvar o registro"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class PesquisasApi(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):

        pesquisas = None

        serializer_paginacao = PesquisaPaginacaoSerializer(data=request.data)

        if serializer_paginacao.is_valid():
            pesquisas = filtrar_pesquisas(
                user_id=request.user.id, filtros=serializer_paginacao.data["filtros"]
            )

        else:
            pesquisas = filtrar_pesquisas(user_id=request.user.id)

        por_pagina = serializer_paginacao.data["quantidade"]

        pagina = serializer_paginacao.data["pagina"]
        if pagina <= 0:
            pagina = 1

        paginacao = Paginator(pesquisas, por_pagina)
        registros = paginacao.get_page(pagina)

        res_data = {
            "registros": PesquisaSerializar(registros.object_list, many=True).data,
            "total": paginacao.count,
            "porPagina": por_pagina,
            "paginas": paginacao.num_pages,
            "pagina": pagina,
        }

        return Response(res_data, status=status.HTTP_200_OK)


class PesquisaApi(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request, id_pesquisa, format=None):
        if (id_pesquisa > 0):
            try:
                p = Pesquisa.objects.get(pk=id_pesquisa)
                p.delete()
                return Response(status=status.HTTP_200_OK)

            except Pesquisa.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "ID inválido"}, status=status.HTTP_400_NOT_FOUND)