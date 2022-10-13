from django.conf import settings
from django.urls import path

from pesquisas import views

app_name = 'pesquisas'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('pesquisaHome/', views.pesquisaHome, name='pesquisaHome'),
    path('pesquisaCadastrar/', views.pesquisaCadastrar, name='pesquisaCadastrar'),
    path('pesquisaListar/', views.pesquisaListar, name='pesquisaListar'),
    path('pesquisaGrafico/', views.pesquisaGrafico, name='pesquisaGrafico'),
]
