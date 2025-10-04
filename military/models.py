from django.db import models

class MilitaryBase(models.Model):
    name = models.CharField(
        max_length=100,verbose_name="Nome")
    war_name = models.CharField(
        max_length=100,
        verbose_name="Nome de guerra")
    military_rank = models.CharField(max_length=50,
        verbose_name="Posto/Graduação")
    year_entry = models.CharField(max_length=50,
        blank=True,
        null=True,
        verbose_name="Barra")
    cpf = models.CharField(max_length=50,
        unique=True,
        verbose_name="CPF")
    phone = models.CharField(max_length=15, 
        verbose_name="Telefone")
    email = models.EmailField(unique=True,
        verbose_name="E-mail")
    address = models.CharField(max_length=255,
        verbose_name="Endereço")
    city = models.CharField(max_length=100,
        verbose_name="Cidade")
    state = models.CharField(max_length=100,
        verbose_name="Estado")
    date_of_birth = models.DateField()
    id_number = models.CharField(max_length=20,
        unique=True,
        verbose_name="ID")
    status = models.CharField(max_length=50,
        verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True,
        verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True,
        verbose_name="Atualizado em")

    class Meta:
        ordering = ['name']
        verbose_name = "Militar"
        verbose_name_plural = "Militares"

    def __str__(self):
        return self.name
    
