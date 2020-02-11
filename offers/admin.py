from django.contrib import admin
from .models import AllProduct


class AllProductAdmin(admin.ModelAdmin):
  list_display = ('id', 'product_name', 'category', 'is_published')
  list_display_links = ('id', 'product_name')
  list_filter = ('category',)
  list_editable = ('is_published',)
  search_fields = ('product_name',)
  list_per_page = 25

admin.site.register(AllProduct, AllProductAdmin)