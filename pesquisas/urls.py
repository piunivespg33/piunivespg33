from django.urls import path
from pesquisas import views

urlpatterns = [
    path("api/pesquisas/carregar", views.CarregaPesquisaApi.as_view(), name="apiCarregaPequisa"),
    path("api/pesquisas", views.PesquisasApi.as_view(), name="apiPequisas"),
    path("api/pesquisa/<int:id_pesquisa>", views.PesquisaApi.as_view(), name="apiPequisa"),
]
