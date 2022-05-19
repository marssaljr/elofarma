from django.contrib import admin
from .models import Pills, Delivery

@admin.register(Pills)
class PillsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image','quantity', 'description', 'category')
    list_editable = ('price', 'category')
    list_filter = ('name', 'price', 'category')

#admin.site.register(Image)
admin.site.register(Delivery)

