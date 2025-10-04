from django.db import models
from military.models import MilitaryBase

class Weapon(models.Model):
    TYPE_CHOICES = [
        ('Pistola', 'Pistola'),
        ('Carabina', 'Carabina'),
        ('Fuzil', 'Fuzil'),
    ]
    MODEL_TYPE_CHOICES = [
        ('PT100', 'PT100'),
        ('PT840', 'PT840'),
        ('IA2', 'IA2'),
        ('SMT40', 'SMT40'),
    ]
    CALIBER_CHOICES = [
        ('40mm', '40mm'),
        ('5.56mm', '5.56mm'),
        ('7.62mm', '7.62mm'),
    ]
    STATUS_CHOICES = [
        ('Cautela Provisória', 'Cautela Provisória'),
        ('Cautela Permanente', 'Cautela Permanente'),
        ('Reserva', 'Reserva'),
    ]

    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        verbose_name='Tipo'
    )
    model_type = models.CharField(
        max_length=50,
        choices=MODEL_TYPE_CHOICES,
        default='PT100',
        verbose_name='Modelo'
    )
    serial_number = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Número de Série'
    )
    caliber = models.CharField(
        max_length=50,
        choices=CALIBER_CHOICES,
        verbose_name='Calibre'
    )
    manufacturer = models.CharField(
        max_length=100,
        verbose_name='Fabricante'
    )
    owner = models.ForeignKey(
        'military.MilitaryBase',
        on_delete=models.CASCADE,
        verbose_name='Portador'
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        verbose_name='Status'
    )
    
    class Meta:
        verbose_name = 'Arma'
        verbose_name_plural = 'Armas'
        ordering = ['type']

    def __str__(self):
        return f"{self.model_type} - {self.serial_number}"
