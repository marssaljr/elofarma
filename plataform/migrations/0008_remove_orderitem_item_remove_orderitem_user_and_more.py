# Generated by Django 4.0.1 on 2022-05-18 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataform', '0007_cart_ordered_cart_session_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='item',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]