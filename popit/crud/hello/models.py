from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
 
class Person(models.Model):
    name = models.CharField(max_length=250, blank=False)
    surname = models.CharField(max_length=250, blank=False, default='')
    email = models.CharField(max_length=250, choices=[('Трудоустроенный', 'Трудоустроенный'), ('Безработный', 'Безработный')], default='Безработный', blank=False)
    age = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(18), MaxValueValidator(65)])  # Добавляем поле для возраста с ограничениями