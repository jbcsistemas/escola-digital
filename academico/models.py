from django.db import models
from django.utils.translation import gettext_lazy as _
from pessoa.models import Pessoa


class Disciplina(models.Model):
    nome = models.CharField(max_length=40)
    carga_horaria = models.IntegerField('Carga Horária')


class GradeCurricular(models.Model):
    disciplinas = models.OneToOneField(
        Disciplina,
        on_delete=models.CASCADE,
    )


class AreaDoConhecimento(models.Model):
    nome = models.CharField(max_length=40)


class Curso(models.Model):

    class Turno(models.TextChoices):
        MATUTINO = 'MT', _('Matutino')
        NOTURNO = 'NT', _('Noturno')
        VESPERTINO = 'VP', _('Vespertino')

    nome = models.CharField(max_length=40)
    area = models.OneToOneField(
        AreaDoConhecimento,
        on_delete=models.SET_NULL,
        null=True,
    )
    turno = models.CharField(
        max_length=2,
        choices=Turno.choices,
    )


class SerieModulo(models.Model):
    TURMA = (
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
    )
    nome = models.CharField(
        verbose_name='Série/Ano, módulo, semestre, eixo temático',
        max_length=40,
    )
    turma = models.CharField(
        max_length=1,
        choices=TURMA,
        default='a',
    )
    curso = models.OneToOneField(
        Curso,
        on_delete=models.CASCADE,
    )
    grade = models.OneToOneField(
        GradeCurricular,
        on_delete=models.SET_NULL,
        null=True,
    )


class Aluno(Pessoa):
    matricula = models.CharField(
        verbose_name='Matrícula',
        max_length=15,
        null=True,
    )
    # Turma será relações. CharField será usado
    # temporariamente até que sejam definidas as regras
    # de negócio.
    curso = models.ForeignKey(
        Curso,
        on_delete=models.SET_NULL,
        null=True,
    )
    serie_modulo = models.ForeignKey(
        SerieModulo,
        on_delete=models.SET_NULL,
        null=True,
    )


class Professor(Pessoa):
    pass
