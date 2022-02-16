from django.contrib import admin
from FitnessStore.models import Catagory, subCatagory, products
# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display = ('id','pname', 'pdesc', 'prate', 'pimage', 'subcat')


admin.site.register(products, productAdmin)