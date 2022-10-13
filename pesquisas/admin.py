from django.contrib import admin

from .models import Pesquisa


@admin.register(Pesquisa)
class PequisaAdmin(admin.ModelAdmin):
    list_display = ('autores', 'titulo', 'fonte_artigo', 'palavras_chave', 
                    'resumo_artigo', 'endereco_autores', 'instituicao_autores', 
                    'agencia_fomento', 'contagem_citacoes', 'ano_publicacao', 
                    'areas_pesquisa')
    search_fields = ('autores', 'titulo', 'palavras_chave')
    data_hierarchy = 'ano_publicacao'
    ordering = ('autores', 'titulo', 'palavras_chave')
