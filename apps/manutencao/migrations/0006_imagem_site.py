# Generated by Django 3.2 on 2021-06-22 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manutencao', '0005_alter_empresa_geo_localizacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem_site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='temp/')),
                ('rodape', models.BooleanField(default=False)),
            ],
        ),
    ]
