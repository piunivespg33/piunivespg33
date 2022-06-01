from django.urls import path
from pesquisas import views

urlpatterns = [
    path(
        "pesquisas/cadastrarPesquisa/",
        views.cadastrarPesquisa,
        name="cadastrarPesquisa",
    ),
    path(
        "pesquisas/consultarPesquisa/",
        views.consultarPesquisa,
        name="consultarPesquisa",
    ),
    path("pesquisas/<int:id>", views.deletarPesquisa, name="deletarPesquisa"),
    path(
        "pesquisas/melhoriasFuturas/", views.melhoriasFuturas, name="melhoriasFuturas"
    ),
    path("api/pesquisas/carregar", views.CarregaPesquisaApi.as_view(), name="apiCarregaPequisa"),
    path("api/pesquisas", views.PesquisasApi.as_view(), name="apiPequisa"),
    
]
