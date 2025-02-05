from django.contrib import admin
from django.utils.safestring import mark_safe

from hexashop_app.models import Category, Product, ProductImage , Type


# Register your models here.

admin.site.site_header = 'Hexashop Admin Panel'
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

class ProductInline(admin.TabularInline):
    model = Product
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'discount' , 'price' , 'category' ,
                    'color' , 'brand' , 'description', 'type' , 'image']
    list_editable = ['discount' , 'price' , 'category' , 'color' ,
                         'brand' , 'description' , 'name']
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('name' , )}
    def image(self , product):
         images = product.images.all()
         if images:
             return mark_safe(f'<img src="{images[0].image.url}" width="50" height="50" />')
         return '-'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name' , 'slug']
    prepopulated_fields = {'slug': ('name' , )}

admin.site.register(Category , CategoryAdmin)
admin.site.register(Product  , ProductAdmin)
admin.site.register(Type)