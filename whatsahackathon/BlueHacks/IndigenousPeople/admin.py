from django.contrib import admin
from .models import CultureInfo, Product1, Product2, Product3
# Register your models here.


class CultureInfoAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'image_url', 'webpage', 'pic1', 'pic2', 'pic3')


class Product1Admin(admin.ModelAdmin):
	list_display = ('name', 'description', 'image_url', 'price')


class Product2Admin(admin.ModelAdmin):
	list_display = ('name', 'description', 'image_url', 'price')


class Product3Admin(admin.ModelAdmin):
	list_display = ('name', 'description', 'image_url', 'price')


admin.site.register(Product1, Product1Admin)
admin.site.register(Product2, Product2Admin)
admin.site.register(Product3, Product3Admin)
admin.site.register(CultureInfo, CultureInfoAdmin)
