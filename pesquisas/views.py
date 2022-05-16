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
        publication_type = item.get('Publication Type')
        authors = item.get('Authors')
        book_authors = item.get('Book Authors')
        book_editors = item.get('Book Editors')
        book_group_authors = item.get('Book Group Authors')
        author_full_names = item.get('Author Full Names')
        book_author_full_names = item.get('Book Author Full Names')
        group_authors = item.get('Group Authors')
        article_title = item.get('Article Title')
        source_title = item.get('Source Title')
        book_series_title = item.get('Book Series Title')
        book_series_subtitle = item.get('Book Series Subtitle')
        language = item.get('Language')
        document_type = item.get('Document Type')
        conference_title = item.get('Conference Title')
        conference_date = item.get('Conference Date')
        conference_location = item.get('Conference Location')
        conference_sponsor = item.get('Conference Sponsor')
        conference_host = item.get('Conference Host')
        author_keywords = item.get('Author Keywords')
        keywords_plus = item.get('Keywords Plus')
        abstract = item.get('Abstract')
        addresses = item.get('Addresses')
        affiliations = item.get('Affiliations')
        reprint_addresses = item.get('Reprint Addresses')
        email_addresses = item.get('Email Addresses')
        researcher_ids = item.get('Researcher Ids')
        orcids = item.get('ORCIDs')
        funding_orgs = item.get('Funding Orgs')
        funding_text = item.get('Funding Text')
        cited_references = item.get('Cited References')
        cited_reference_count = item.get('Cited Reference Count')
        times_cited_wos_core = item.get('Times Cited WoS Core')
        times_cited_all_databases = item.get('Times Cited All Databases')
        day_usage_count = item.get('180 Day Usage Count')
        since_2013_usage_count = item.get('Since 2013 Usage Count')
        publisher = item.get('Publisher')
        publisher_city = item.get('Publisher City')
        publisher_address = item.get('Publisher Address')
        issn = item.get('ISSN')
        eissn = item.get('eISSN')
        isbn = item.get('ISBN')
        journal_abbreviation = item.get('Journal Abbreviation')
        journal_iso_abbreviation = item.get('Journal ISO Abbreviation')
        publication_date = item.get('Publication Date')
        publication_year = item.get('Publication Year')
        volume = item.get('Volume')
        issue = item.get('Issue')
        part_number = item.get('Part Number')
        supplement = item.get('Supplement')
        special_issue = item.get('Special Issue')
        meeting_abstract = item.get('Meeting Abstract')
        start_page = item.get('Start Page')
        end_page = item.get('End Page')
        article_number = item.get('Article Number')
        doi = item.get('DOI')
        book_doi = item.get('Book DOI')
        early_access_date = item.get('Early Access Date')
        number_of_pages = item.get('Number of Pages')
        wos_categories = item.get('WoS Categories')
        web_of_science_index = item.get('Web of Science Index')
        research_areas = item.get('Research Areas')
        ids_number = item.get('IDS Number')
        pubmed_id = item.get('Pubmed Id')
        open_access_designations = item.get('Open Access Designations')
        highly_cited_status = item.get('Highly Cited Status')
        hot_paper_status = item.get('Hot Paper Status')
        date_of_export = item.get('Date of Export')
        unique_wos_id = item.get('UT (Unique WOS ID)')
        obj = Pesquisa(
            publication_type = publication_type,
            authors = authors,
            book_authors = book_authors,
            book_editors = book_editors,
            book_group_authors = book_group_authors,
            author_full_names = author_full_names,
            book_author_full_names = book_author_full_names,
            group_authors = group_authors,
            article_title = article_title,
            source_title = source_title,
            book_series_title = book_series_title,
            book_series_subtitle = book_series_subtitle,
            language = language,
            document_type = document_type,
            conference_title = conference_title,
            conference_date = conference_date,
            conference_location = conference_location,
            conference_sponsor = conference_sponsor,
            conference_host = conference_host,
            author_keywords = author_keywords,
            keywords_plus = keywords_plus,
            abstract = abstract,
            addresses = addresses,
            affiliations = affiliations,
            reprint_addresses = reprint_addresses,
            email_addresses = email_addresses,
            researcher_ids = researcher_ids,
            orcids = orcids,
            funding_orgs = funding_orgs,
            funding_text = funding_text,
            cited_references = cited_references,
            cited_reference_count = cited_reference_count,
            times_cited_wos_core = times_cited_wos_core,
            times_cited_all_databases = times_cited_all_databases,
            day_usage_count = day_usage_count,
            since_2013_usage_count = since_2013_usage_count,
            publisher = publisher,
            publisher_city = publisher_city,
            publisher_address = publisher_address,
            issn = issn,
            eissn = eissn,
            isbn = isbn,
            journal_abbreviation = journal_abbreviation,
            journal_iso_abbreviation = journal_iso_abbreviation,
            publication_date = publication_date,
            publication_year = publication_year,
            volume = volume,
            issue = issue,
            part_number = part_number,
            supplement = supplement,
            special_issue = special_issue,
            meeting_abstract = meeting_abstract,
            start_page = start_page,
            end_page = end_page,
            article_number = article_number,
            doi = doi,
            book_doi = book_doi,
            early_access_date = early_access_date,
            number_of_pages = number_of_pages,
            wos_categories = wos_categories,
            web_of_science_index = web_of_science_index,
            research_areas = research_areas,
            ids_number = ids_number,
            pubmed_id = pubmed_id,
            open_access_designations = open_access_designations,
            highly_cited_status = highly_cited_status,
            hot_paper_status = hot_paper_status,
            date_of_export = date_of_export,
            unique_wos_id = unique_wos_id,
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
