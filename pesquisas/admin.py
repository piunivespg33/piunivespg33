from django.contrib import admin
from pesquisas.models import Pesquisa

class PesquisaAdmin(admin.ModelAdmin):
    class Meta:
        model = Pesquisa
        fields = ['name', 'address', 'country', 'publication_title', 'publication_Number', 'year', 'match', 'type_organization']
        search_fields = ['publication_title']

admin.site.register(Pesquisa, PesquisaAdmin)
