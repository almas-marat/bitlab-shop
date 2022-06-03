from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name='Имя категории', max_length=50, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField('Название продукта', max_length=50)
    price = models.IntegerField('Цена')
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.pk) + ') ' + self.title