# Generated by Django 3.2 on 2021-05-04 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0005_alter_iten_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iten',
            name='imagem',
            field=models.ImageField(upload_to='fotos/'),
        ),
    ]
