from typing import List
from pesquisas.models import Pesquisa
from django.db.models import Q, QuerySet


def filtrar_pesquisas(filtros: dict) -> List[QuerySet]:
    """
    Procura no banco de dados todas as Pesquisas conforme os filtros 
    especificados, seguindo o formato
    "Campo" : "valor" (Campo=valor)
    "Campo__istartswith": "Valor" (Campo LIKE 'Valor%')
    "Campo__iendswith": "Valor" (Campo LIKE 'Valor%')
    "Campo__contains": "Valor" (Campo LIKE '%Valor%')

    :param filtros: Dicionário com a lista de filtros
    :type filtros: dict
    :return: Lista de Pesquisas encontradas conforme o filtro
    :rtype: Queryset
    """
    
    return Pesquisa.objects.filter(Q(**filtros)).all()
