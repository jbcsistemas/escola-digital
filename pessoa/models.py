from django.db import models


class Pessoa(models.Model):
    nome_completo = models.CharField(
        verbose_name='Nome Completo',
        max_length=60,
    )
    rg = models.CharField(
        max_length=11,
        blank=True,
    )
    cpf = models.CharField(
        max_length=12,
        blank=True,
    )
    nascimento = models.DateField()
    naturalidade = models.CharField(max_length=45)
    cep = models.CharField(max_length=7)
    endereco = models.CharField(
        verbose_name='Endereço',
        max_length=40,
    )
    numero = models.CharField(
        verbose_name='Número',
        max_length=5,
        default='S/N',
    )
    complemento = models.CharField(max_length=25)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    pais = models.CharField(
        verbose_name='País',
        max_length=20,
        default='Brasil',
    )

    class Meta:
        abstract = True
