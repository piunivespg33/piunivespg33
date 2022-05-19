# Generated by Django 3.2.13 on 2022-05-19 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pesquisa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autores', models.TextField(blank=True, null=True)),
                ('titulo', models.TextField(blank=True, null=True)),
                ('fonte_artigo', models.TextField(blank=True, null=True)),
                ('palavras_chave', models.TextField(blank=True, null=True)),
                ('resumo_artigo', models.TextField(blank=True, null=True)),
                ('endereco_autores', models.TextField(blank=True, null=True)),
                ('instituição_vinculo_autores', models.TextField(blank=True, null=True)),
                ('agencia_fomento', models.TextField(blank=True, null=True)),
                ('contagem_citacoes', models.IntegerField(blank=True, null=True)),
                ('ano_publicacao', models.TextField(blank=True, null=True)),
                ('areas_pesquisa', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
