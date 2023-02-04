from django.contrib import admin
from .models import *
# Register your models here.
class category_admin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Category,category_admin)

class product_admin(admin.ModelAdmin):
    list_display=['name','slug','price','image','stock','availability','created','updated']
    list_editable=['price','stock','availability']
    list_per_page=20
    prepopulated_fields={'slug':('name',)}
admin.site.register(Product,product_admin)