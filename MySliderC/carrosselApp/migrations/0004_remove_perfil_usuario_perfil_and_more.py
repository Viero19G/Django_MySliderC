# Generated by Django 4.2.5 on 2023-09-26 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carrosselApp', '0003_remove_setor_tela_setor_grade_remove_grade_conteudo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil_usuario',
            name='perfil',
        ),
        migrations.RemoveField(
            model_name='perfil_usuario',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='setor',
        ),
        migrations.AddField(
            model_name='conteudo',
            name='usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
        migrations.AddField(
            model_name='grade',
            name='usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
        migrations.AddField(
            model_name='grade',
            name='usuariosEdit',
            field=models.ManyToManyField(blank=True, related_name='grades_editadas', to=settings.AUTH_USER_MODEL, verbose_name='Editores de Grade'),
        ),
        migrations.AddField(
            model_name='setor',
            name='membros',
            field=models.ManyToManyField(blank=True, related_name='setores_membros', to=settings.AUTH_USER_MODEL, verbose_name='Membros do Setor'),
        ),
        migrations.AlterField(
            model_name='conteudo',
            name='descricao',
            field=models.CharField(max_length=200, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='conteudo',
            name='image',
            field=models.ImageField(upload_to='pics/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='conteudo',
            name='sub_title',
            field=models.CharField(max_length=200, verbose_name='Sub-Título'),
        ),
        migrations.AlterField(
            model_name='conteudo',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='conteudo',
            field=models.ManyToManyField(blank=True, to='carrosselApp.conteudo', verbose_name='Conteúdo'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='sub_title',
            field=models.CharField(max_length=200, verbose_name='Sub-Título'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='setor',
            name='grade',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='carrosselApp.grade', verbose_name='Grade'),
        ),
        migrations.AlterField(
            model_name='setor',
            name='nome',
            field=models.CharField(max_length=180, verbose_name='Nome'),
        ),
        migrations.DeleteModel(
            name='Perfil',
        ),
        migrations.DeleteModel(
            name='Perfil_Usuario',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
