# Generated by Django 4.2.5 on 2023-10-05 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrosselApp', '0011_conteudo_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conteudo',
            name='usuario',
        ),
    ]
