from django.contrib import admin
from .models import Client,Product,ListProduct

class ClientAdmin(admin.ModelAdmin):
	list_display = ['id','name']
	list_display_links = ['id','name']
	prepopulated_fields = {'slug':('name',)}
	list_per_page = 25
	can_delete= False

	def has_delete_permission(self, request, obj=None):
		return False

class ListProductAdmin(admin.ModelAdmin):
	list_display = ('id', 'name','category','available')
	list_display_links = ('id', 'name')
	list_filter = ('category',)
	search_fields = ('name',)
	list_editable = ['available',]
	list_per_page = 25


class ProductAdmin(admin.ModelAdmin):
	list_display = ['id','user','product','price','created','updated']
	fieldsets = (
        (None, {'fields': ('user','client','product','slug','price')}),
	)
	list_display_links = ['id','product', 'user']
	search_fields = ('user__username', 'product__name')
	list_filter = ('user__username', 'product__name')
	list_editable = ['price',]
	prepopulated_fields = {'slug':('product',)}
	list_per_page = 25



admin.site.register(Client,ClientAdmin)
admin.site.register(ListProduct,ListProductAdmin)
admin.site.register(Product,ProductAdmin)
