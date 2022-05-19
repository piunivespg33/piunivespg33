from django.db import models


class Pesquisa(models.Model):
    #pesquisa_id   = models.AutoField(primary_key=True)
    autores = models.TextField(null=True, blank=True)
    titulo = models.TextField(null=True, blank=True)
    fonte_artigo = models.TextField(null=True, blank=True)
    palavras_chave = models.TextField(null=True, blank=True)
    resumo_artigo = models.TextField(null=True, blank=True)
    endereco_autores = models.TextField(null=True, blank=True)
    instituição_vinculo_autores = models.TextField(null=True, blank=True)
    agencia_fomento = models.TextField(null=True, blank=True)
    contagem_citacoes = models.IntegerField(blank=True, null=True)
    ano_publicacao = models.TextField(null=True, blank=True)
    areas_pesquisa = models.TextField(null=True, blank=True)
