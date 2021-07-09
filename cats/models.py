from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from django.core import validators
# Create your models here.


class Breed(models.Model):
      name = models.CharField(max_length=200)

      def __str__(self):
            return self.name

class Cat(models.Model):
      nickname = models.CharField(max_length=100,verbose_name='Cat name',
            help_text='name of the cat (min 3 characters)',
            validators=[MinLengthValidator(3,'Cat name should be at least 3 characters')])
      breed = models.ForeignKey('Breed',on_delete=models.CASCADE,null=False)
      weight = models.FloatField(verbose_name='Weight (kg)',
                  validators=[MinValueValidator(0.0)])
      foods = models.CharField(max_length=200, null=True, blank=True)
      def __str__(self):
            return self.nickname