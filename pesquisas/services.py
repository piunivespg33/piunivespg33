from typing import List
from pesquisas.models import Pesquisa
from django.db.models import Q, QuerySet


def filtrar_pesquisas(user_id: int, filtros: List[dict] = None) -> List[QuerySet]:
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
    query = Pesquisa.objects
    if filtros:
        filtros_dict = {}
        for filtro in filtros:
            filtros_dict[f"{filtro['campo']}__{filtro['tipo']}"] = filtro["valor"]
        return Pesquisa.objects.filter(Q(**filtros_dict)).filter(user_id=user_id).all()
    else:
        return query.filter(user_id=user_id).all()
