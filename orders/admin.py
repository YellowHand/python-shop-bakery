from django.contrib import admin
from .models import Order, OrderItem

class OrderItemAdmin(admin.TabularInline):
	model = OrderItem
	fieldsets = [
	('Code',{'fields':['code']}),
	('Product',{'fields':['product'],}),
	('Quantity',{'fields':['quantity'],}),
	('Price',{'fields':['price'],}),
	]
	readonly_fields = ['code','product','quantity','price']
	can_delete= False
	max_num = 0
	template = 'admin/order/tabular.html'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ['id','customerNumber','created', 'completed']
	list_display_links = ('id','customerNumber')
	list_per_page = 25
	search_fields = ['id','customerNumber']
	list_filter = ['created', 'completed']
	readonly_fields = ['id','total','created','customerNumber','email','address','city',
					'postCode','country','shippingName','shippingAddress','shippingCity','shippingPostcode','shippingCountry', 'deliveryPhone', 'phone', 'deliveryMonday', 'deliveryTuesday', 'deliveryWednesday', 'deliveryThursday', 'deliveryFriday', 'deliverySaturday', 'message']
	fieldsets = [
	('ORDER INFORMATION',{'fields': ['id','total','created', 'completed']}),
	('CUSTOMER INFORMATION', {'fields': ['email','address','postCode','city','country','phone']}),
	('DELIVERY INFORMATION', {'fields': ['shippingName','shippingAddress','shippingPostcode','shippingCity','shippingCountry', 'deliveryPhone', 'deliveryMonday', 'deliveryTuesday', 'deliveryWednesday', 'deliveryThursday', 'deliveryFriday', 'deliverySaturday', 'message', 'customerNumber']}),
	]

	inlines = [
		OrderItemAdmin,
	]

	
	def has_delete_permission(self, request, obj=None):
		return False

	def has_add_permission(self, request):
		return False

