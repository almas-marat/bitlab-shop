from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name='Имя категории', max_length=50, unique=True)

class Product(models.Model):
    title = models.CharField('Название продукта', max_length=50)
    price = models.IntegerField('Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title
