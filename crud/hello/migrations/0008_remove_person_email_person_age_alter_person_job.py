# Generated by Django 5.0.6 on 2024-06-06 13:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_rename_age_person_job_alter_person_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='email',
        ),
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(65)]),
        ),
        migrations.AlterField(
            model_name='person',
            name='job',
            field=models.CharField(choices=[('Трудоустроенный', 'Трудоустроенный'), ('Безработный', 'Безработный')], default='Безработный', max_length=250),
        ),
    ]
