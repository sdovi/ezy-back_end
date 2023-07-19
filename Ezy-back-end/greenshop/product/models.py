from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Info(models.Model):
    title = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена товара")
    description = models.TextField()
    photo = models.CharField(max_length=300)
    photo2 = models.CharField(max_length=300)
    photo3 = models.CharField(max_length=300)
    photo4 = models.CharField(max_length=300)
    photo5 = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"

class Orders(models.Model):
    title = models.CharField("ФИО", max_length=50)
    price = models.IntegerField("Номер")
    EMail = models.TextField('Email')
    description = models.TextField('Комментарий к заказу')
    shop = models.TextField('Продукт')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
