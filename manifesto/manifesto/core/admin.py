from django.contrib import admin
from core.models import *

# Register your models here.
@admin.register(MainBanner)

class MainBannerAdmin(admin.ModelAdmin):
    list_display=['id','name','file','updated_date','created_date']

    search_fields = ['id','name']
    list_editable=['file']

    class Meta:
        model = MainBanner
@admin.register(Logo)

class LogoAdmin(admin.ModelAdmin):
    list_display=['id','name','file','updated_date','created_date']

    search_fields = ['id','name']
    list_editable=['file']

    class Meta:
        model = Logo

@admin.register(Food)

class FoodAdmin(admin.ModelAdmin):
    list_display=['id','order','name','price','file','updated_date','created_date']

    search_fields = ['id','name']
    list_editable=['file','price']

    class Meta:
        model = Food
@admin.register(Dessert)

class DessertAdmin(admin.ModelAdmin):
    list_display=['id','order','name','price','file','updated_date','created_date']

    search_fields = ['id','name']
    list_editable=['file','price']

    class Meta:
        model = Dessert
@admin.register(BussinessLunch)

class BussinessLunchAdmin(admin.ModelAdmin):
    list_display=['id','order','name','price','file','updated_date','created_date']

    search_fields = ['id','name']
    list_editable=['file','price']

    class Meta:
        model = BussinessLunch
@admin.register(Drink)

class DrinkAdmin(admin.ModelAdmin):
    list_display=['id','order','name','price','file','updated_date','created_date']

    search_fields = ['id','name']
    list_editable=['file','price']

    class Meta:
        model = Drink
@admin.register(TextGoal)

class TextGoalAdmin(admin.ModelAdmin):
    list_display=['id','name','description','updated_date','created_date']

    search_fields = ['id','name']
    list_editable=['name','description']

    class Meta:
        model = TextGoal
@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display=['id','order','link','icon','updated_date','created_date']

    search_fields = ['order','link','icon']
    list_editable=['link','icon',]

    class Meta:
        model = SocialMedia