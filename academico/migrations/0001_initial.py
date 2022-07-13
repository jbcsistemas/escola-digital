# Generated by Django 3.2 on 2022-07-10 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaDoConhecimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('turno', models.CharField(choices=[('MT', 'Matutino'), ('NT', 'Noturno'), ('VP', 'Vespertino')], max_length=2)),
                ('area', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='academico.areadoconhecimento')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('carga_horaria', models.IntegerField(verbose_name='Carga Horária')),
            ],
        ),
        migrations.CreateModel(
            name='GradeCurricular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciplinas', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='academico.disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=60, verbose_name='Nome Completo')),
                ('rg', models.CharField(blank=True, max_length=11)),
                ('cpf', models.CharField(blank=True, max_length=12)),
                ('nascimento', models.DateField()),
                ('naturalidade', models.CharField(max_length=45)),
                ('cep', models.CharField(max_length=7)),
                ('endereco', models.CharField(max_length=40, verbose_name='Endereço')),
                ('numero', models.CharField(default='S/N', max_length=5, verbose_name='Número')),
                ('complemento', models.CharField(max_length=25)),
                ('bairro', models.CharField(max_length=30)),
                ('cidade', models.CharField(max_length=30)),
                ('pais', models.CharField(default='Brasil', max_length=20, verbose_name='País')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SerieModulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, verbose_name='Série/Ano, módulo, semestre, eixo temático')),
                ('turma', models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], default='a', max_length=1)),
                ('curso', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='academico.curso')),
                ('grade', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='academico.gradecurricular')),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=60, verbose_name='Nome Completo')),
                ('rg', models.CharField(blank=True, max_length=11)),
                ('cpf', models.CharField(blank=True, max_length=12)),
                ('nascimento', models.DateField()),
                ('naturalidade', models.CharField(max_length=45)),
                ('cep', models.CharField(max_length=7)),
                ('endereco', models.CharField(max_length=40, verbose_name='Endereço')),
                ('numero', models.CharField(default='S/N', max_length=5, verbose_name='Número')),
                ('complemento', models.CharField(max_length=25)),
                ('bairro', models.CharField(max_length=30)),
                ('cidade', models.CharField(max_length=30)),
                ('pais', models.CharField(default='Brasil', max_length=20, verbose_name='País')),
                ('matricula', models.CharField(max_length=15, null=True, verbose_name='Matrícula')),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='academico.curso')),
                ('serie_modulo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='academico.seriemodulo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]