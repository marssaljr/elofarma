# Generated by Django 4.0.1 on 2022-01-12 20:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataform', '0002_remove_pills_buyday_remove_pills_buytime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pills',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='pills',
            name='category',
            field=models.CharField(choices=[('G', 'Genérico'), ('S', 'Similar'), ('GS', 'Genérico e Similar'), ('N', '')], max_length=2),
        ),
    ]
