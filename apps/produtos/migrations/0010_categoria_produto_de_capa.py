# Generated by Django 3.2 on 2021-06-09 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0009_auto_20210607_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='produto_de_capa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='produtos.iten'),
        ),
    ]