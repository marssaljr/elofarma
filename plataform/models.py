from django.db import models
from django.contrib.auth.models import User
import datetime

# class Image(models.Model):
#     img = models.ImageField(upload_to='img')
#     def __str__(self) -> str:
#         return self.img.url

class Pills(models.Model):
    choices = (
        ('G', 'Genérico'),
        ('S', 'Similar'),
        ('GS', 'Genérico e Similar'),
        ('N', ''),
    )
    name = models.CharField(max_length=200)
    date = models.DateField(("Date"), default=datetime.date.today)
    image = models.ImageField(upload_to='img')
    price = models.FloatField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=2, choices=choices)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

# class OrderItem(models.Model):
#     user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
#     ordered = models.BooleanField(default=True)
#     item = models.ForeignKey(Pills, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)

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

# class Cart(models.Model):
#   user        = models.ForeignKey(User,null=True, blank=True,on_delete=models.CASCADE)
#   products    = models.ManyToManyField(OrderItem, blank=True)
#   subtotal    = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
#   total       = models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
#   updated     = models.DateTimeField(auto_now=True)
#   timestamp   = models.DateTimeField(auto_now_add=True)
#   ordered     = models.BooleanField(default=False)
#   session_key = models.CharField(max_length=40, null=True)