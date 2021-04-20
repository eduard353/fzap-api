from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mark(models.Model):

    mark_name = models.CharField(max_length=50)

    def __str__(self):
        return self.mark_name

class Model(models.Model):

    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, related_name='mark_models')
    model_name = models.CharField(max_length=50)

    def __str__(self):
        #return str(self.mark) + ' ' + self.model_name
        return str(self.model_name)

class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_orders')
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='model_orders')
    year = models.PositiveIntegerField()
    vin = models.CharField(max_length=17)
    order_details = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class Shop(models.Model):

    shop_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.shop_name

class Answer(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_answers')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shop_answers')
    answer_details = models.CharField(max_length=500)
    price = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
