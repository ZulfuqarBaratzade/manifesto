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
    