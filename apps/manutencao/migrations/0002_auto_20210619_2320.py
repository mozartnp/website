# Generated by Django 3.2 on 2021-06-20 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manutencao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_da_empresa', models.CharField(max_length=50)),
                ('telefone1', models.CharField(max_length=15)),
                ('telefone2', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('endereco', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
                ('geo_localizacao', models.URLField()),
                ('texto', models.TextField()),
                ('logo', models.ImageField(upload_to='temp/')),
            ],
        ),
        migrations.DeleteModel(
            name='TextoEmpresa',
        ),
    ]
