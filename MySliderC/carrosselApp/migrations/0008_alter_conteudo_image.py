# Generated by Django 4.2.5 on 2023-09-27 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrosselApp', '0007_alter_setor_membros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conteudo',
            name='image',
            field=models.FileField(upload_to='pics/%Y/%m/%d/'),
        ),
    ]
