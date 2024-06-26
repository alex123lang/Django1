from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, **NULLABLE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'price', 'created_at', 'updated_at']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name
