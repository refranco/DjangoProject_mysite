from django.db import models
from django.core.validators import MinLengthValidator


class Make(models.Model):
      name = models.CharField(
            max_length=200,
            help_text='Ingrese un fabricante de autos (ej. Audi)',
            validators=[MinLengthValidator(2,'nombre fabricante debe ser mas grande que 1 caracter')],
            verbose_name='Nombre Fabricante' )

      def __str__(self):
          return self.name

class Auto(models.Model):
      nickname = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Apodo debe ser mas grande de 1 caracter")]
      )
      mileage = models.PositiveIntegerField()
      make = models.ForeignKey('Make', on_delete=models.CASCADE, null=False)
      comments = models.CharField(max_length=300)

      def __str__(self):
          return self.nickname



