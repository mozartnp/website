# Generated by Django 3.2 on 2021-05-03 17:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_alter_categoria_nome_da_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='iten',
            name='imagem',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='fotos/%d/%m/%Y'),
            preserve_default=False,
        ),
    ]
