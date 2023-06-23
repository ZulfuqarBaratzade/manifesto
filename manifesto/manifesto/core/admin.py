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
