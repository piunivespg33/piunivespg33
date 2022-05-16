from django.urls import path
from pesquisas import views

urlpatterns = [
    path('cadastrarPesquisa/', views.cadastrarPesquisa, name='cadastrarPesquisa'),
    path('consultarPesquisa/', views.consultarPesquisa, name='consultarPesquisa'),
    path('<int:id>', views.deletarPesquisa, name='deletarPesquisa'),
    path('melhoriasFuturas/', views.melhoriasFuturas, name='melhoriasFuturas'),
]