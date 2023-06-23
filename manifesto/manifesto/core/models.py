from django.db import models

# Create your models here.

class AbstractModel(models.Model):
    updated_date=models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='update_date',

    )
    created_date=models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='created_date'
    )
    class Meta:
        abstract = True

class MainBanner(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='name',

    )
    file = models.ImageField(
        default='',
        help_text='',
        verbose_name='Image',
        blank=True,
        upload_to='images/mainbanner',
    )
    def __str__(self):
        return f"Main Banner : {self.name}"
    class Meta:
        verbose_name = "Main Banner"
        verbose_name_plural = "Main Banner"
        ordering = ('name',)
    
class Logo(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='name',

    )
    file = models.ImageField(
        default='',
        help_text='',
        verbose_name='Image',
        blank=True,
        upload_to='images/logo',
    )
    def __str__(self):
        return f"Logo : {self.name}"
    class Meta:
        verbose_name = "Logo"
        verbose_name_plural = "Logo"
        ordering = ('name',)
class Food(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='name',

    )
    price = models.IntegerField(
        default=0,
        blank=True,
        verbose_name='price'
    )
    file = models.ImageField(
        default='',
        help_text='',
        verbose_name='Image',
        blank=True,
        upload_to='images/food',
    )
    def __str__(self):
        return f"Food : {self.name}"
    class Meta:
        verbose_name = "Food"
        verbose_name_plural = "Food"
        ordering = ('name',)
class Dessert(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='name',

    )
    price = models.IntegerField(
        default=0,
        blank=True,
        verbose_name='price'
    )
    file = models.ImageField(
        default='',
        help_text='',
        verbose_name='Image',
        blank=True,
        upload_to='images/dessert',
    )
    def __str__(self):
        return f"Dessert : {self.name}"
    class Meta:
        verbose_name = "Dessert"
        verbose_name_plural = "Dessert"
        ordering = ('name',)
class BussinessLunch(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='name',

    )
    price = models.IntegerField(
        default=0,
        blank=True,
        verbose_name='price'
    )
    file = models.ImageField(
        default='',
        help_text='',
        verbose_name='Image',
        blank=True,
        upload_to='images/bussinesslunch',
    )
    def __str__(self):
        return f"Bussiness Lunch : {self.name}"
    class Meta:
        verbose_name = "Bussiness Lunch"
        verbose_name_plural = "Bussiness Lunch"
        ordering = ('name',)
class Drink(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='name',

    )
    price = models.IntegerField(
        default=0,
        blank=True,
        verbose_name='price'
    )
    file = models.ImageField(
        default='',
        help_text='',
        verbose_name='Image',
        blank=True,
        upload_to='images/drink',
    )
    def __str__(self):
        return f"Bussiness Lunch : {self.name}"
    class Meta:
        verbose_name = "Drink"
        verbose_name_plural = "Drink"
        ordering = ('name',)