import csv
import io

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from pesquisas.models import Pesquisa


def save_data(data):
    '''
    Salva os dados no banco.
    '''
    aux = []
    for item in data:
        # Atribui valor da coluna ao objeto
        autores = item.get('Autores')
        titulo = item.get('Título')
        fonte_artigo = item.get('Fonte do artigo')
        palavras_chave = item.get('Palavras-chave')
        resumo_artigo = item.get('Resumo do artigo')
        endereco_autores = item.get('Endereço dos Autores')
        instituição_vinculo_autores = item.get('Instituição de vínculo dos autores')
        agencia_fomento = item.get('Agência de Fomento')
        contagem_citacoes = item.get('Contagem do número de citações')
        ano_publicacao = item.get('Ano da publicação')
        areas_pesquisa = item.get('Áreas de pesquisa')
        obj = Pesquisa(
            # Carrega os valores do objeto para objeto da classe pesquisa
            autores = autores,
            titulo = titulo,
            fonte_artigo = fonte_artigo,
            palavras_chave = palavras_chave,
            resumo_artigo = resumo_artigo,
            endereco_autores = endereco_autores,
            instituição_vinculo_autores = instituição_vinculo_autores,
            agencia_fomento = agencia_fomento,
            contagem_citacoes = contagem_citacoes,
            ano_publicacao = ano_publicacao,
            areas_pesquisa = areas_pesquisa,
        )
        aux.append(obj)
    Pesquisa.objects.bulk_create(aux)

def cadastrarPesquisa(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        # Lendo arquivo InMemoryUploadedFile
        file = myfile.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(file))
        # Gerando uma list comprehension
        data = [line for line in reader]
        save_data(data)
        return HttpResponseRedirect(reverse('consultarPesquisa'))

    template_name = 'cadastrarPesquisa.html'
    return render(request, template_name)
 
def consultarPesquisa(request):
    pesquisas = Pesquisa.objects.all()
    context = {
        'pesquisas': pesquisas
    }
    return render(request, 'consultarPesquisa.html', context)


def deletarPesquisa(request, id):
    pesquisa = Pesquisa.objects.get(id=id)
    pesquisa.delete()
    pesquisas = Pesquisa.objects.all()
    context = {
        'pesquisas': pesquisas
    }
    return render(request, 'consultarPesquisa.html', context)

def melhoriasFuturas(request):
    return render(request, 'melhoriasFuturas.html')
