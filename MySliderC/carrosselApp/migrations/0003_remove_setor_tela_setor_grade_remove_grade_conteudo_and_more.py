# Generated by Django 4.2.5 on 2023-09-23 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrosselApp', '0002_rename_carousel_conteudo_rename_tela_grade_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setor',
            name='tela',
        ),
        migrations.AddField(
            model_name='setor',
            name='grade',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='carrosselApp.grade'),
        ),
        migrations.RemoveField(
            model_name='grade',
            name='conteudo',
        ),
        migrations.AddField(
            model_name='grade',
            name='conteudo',
            field=models.ManyToManyField(blank=True, to='carrosselApp.conteudo'),
        ),
    ]
