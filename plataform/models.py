from django.db import models
from django.contrib.auth.models import User
import datetime

class Image(models.Model):
    img = models.ImageField(upload_to='img')
    def __str__(self) -> str:
        return self.img.url

class Pills(models.Model):
    choices = (
        ('G', 'Genérico'),
        ('S', 'Similar'),
        ('GS', 'Genérico e Similar'),
        ('N', ''),
    )
    name = models.CharField(max_length=200)
    date = models.DateField(("Date"), default=datetime.date.today)
    images = models.ManyToManyField(Image)
    price = models.FloatField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=2, choices=choices)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class Delivery(models.Model):
    choices = (('S', 'Segunda'),
               ('T', 'Terça'),
               ('Q', 'Quarta'),
               ('QI', 'Quinta'),
               ('SE', 'Sexta'),
               ('SA', 'Sabado'),
               ('D', 'Domingo'))

    choices_status = (('A', 'Em análise'),
               ('P', 'Pago'),
               ('E', 'Entrege'))
    medicine = models.ForeignKey(Pills, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    buyday = models.CharField(max_length=20)
    buytime = models.TimeField()
    status = models.CharField(max_length=1, choices=choices_status, default="A")

    def __str__(self) -> str:
        return self.user.username

