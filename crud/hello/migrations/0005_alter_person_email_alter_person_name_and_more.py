# Generated by Django 5.0.6 on 2024-05-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_alter_person_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(choices=[('Трудоустроенный', 'Трудоустроенный'), ('Безработный', 'Безработный')], default='Трудоустроенный', max_length=250),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='person',
            name='surname',
            field=models.CharField(default='', max_length=250),
        ),
    ]