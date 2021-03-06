from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Drinks(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    price = models.IntegerField(default=40)
    cup = models.CharField(max_length=3, default="L")
    calorie = models.IntegerField(default=0)
    milk = models.BooleanField(default=False)
    tea = models.BooleanField(default=False)
    cafe = models.BooleanField(default=False)
    juice = models.BooleanField(default=False)
    bubble = models.BooleanField(default=False)
    hotcold = models.IntegerField(default=0)

    def __str__(self):
        return self.name

