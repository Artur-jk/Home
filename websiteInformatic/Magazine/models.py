from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()



# Create your models here.

# **************
# 1 Category
# 2 Product
# 3 Cart Product товар в корзине
# 4 Cart  корзина
# 5 Order
# **************
# 6 Customer
# 7 Specification  Характеристики


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая Цена')

    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.product.title)


class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_product = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая Цена')

    def __str__(self):
        pass

class Notebook(Product):
    diagonal = models.CharField(max_length=255,verbose_name='Диагональ')
    display_type = models.CharField(max_length=255,verbose_name='Тип Дисплея')
    processor_freq = models.CharField(max_length=255,verbose_name='Частота процессора')
    ram = models.CharField(max_length=255,verbose_name='Оперативная память')
    video = models.CharField(max_length=255,verbose_name='Видеокарта')
    time_without_charge = models.CharField(max_length=255,verbose_name='Время работы аккамулятора')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

class Smartphone(Product):
    diagonal = models.CharField(max_length=255, verbose_name='Диагональ')
    display_type = models.CharField(max_length=255, verbose_name='Тип Дисплея')
    resolution=models.CharField(max_length=255,verbose_name='Разрешение')
    accum_volume = models.CharField(max_length=255,verbose_name='Аккумуятор')
    ram = models.CharField(max_length=255, verbose_name='Оперативная память')
    sd = models.BooleanField(default=True)
    sd_volume_max = models.CharField(max_length=255,verbose_name='Объем встроенной памяти')
    main_cam = models.CharField(max_length=255, verbose_name='Главная камера пиксели')
    frontal_cam = models.CharField(max_length=255, verbose_name='фронтальная камера пиксели')
    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона ')
    address = models.CharField(max_length=255, verbose_name='Адресс')

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)#


class Somemodel(models.Model):
    image = models.ImageField()

    def __str__(self):
        return str(self.id)


