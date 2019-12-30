from django.contrib import admin
from mysite.models import Drinks, Store

class DrinksAdmin(admin.ModelAdmin):
    list_display = ('store', 'name', 'price', 'cup', 'calorie', 'milk', 'tea', 'cafe', 'juice', 'bubble', 'hotcold')

admin.site.register(Drinks, DrinksAdmin)
admin.site.register(Store)
