from django.db import models


# Create your models here.

class Product(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    rate = models.FloatField(default=0)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.CharField(max_length=256)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.products.title} - {self.text}'


