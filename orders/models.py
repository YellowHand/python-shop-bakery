from django.db import models

class Order(models.Model):

	CHOICES = (
    (True, "Yes"),
    (False, "No")
)

	total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='GBP Order Total')
	created = models.DateTimeField(auto_now_add=True)
	customerNumber = models.CharField(max_length=250, blank=True)
	email = models.CharField(max_length=250, blank=True)
	address = models.CharField(max_length=250, blank=True)
	city = models.CharField(max_length=250, blank=True)
	postCode = models.CharField(max_length=10, blank=True)
	country = models.CharField(max_length=200, blank=True)
	phone = models.IntegerField(blank=True, default=0)
	shippingName = models.CharField(max_length=250, blank=True)
	shippingAddress = models.CharField(max_length=250, blank=True)
	shippingCity = models.CharField(max_length=250, blank=True)
	shippingPostcode = models.CharField(max_length=10, blank=True)
	shippingCountry = models.CharField(max_length=200, blank=True)
	deliveryPhone = models.IntegerField(blank=True, default=0)
	deliveryMonday = models.BooleanField(default=False)
	deliveryTuesday = models.BooleanField(default=False)
	deliveryWednesday = models.BooleanField(default=False)
	deliveryThursday = models.BooleanField(default=False)
	deliveryFriday = models.BooleanField(default=False)
	deliverySaturday = models.BooleanField(default=False)
	message = models.TextField(blank=True)
	completed = models.BooleanField(default=False, choices=CHOICES)




	class Meta:
		db_table = 'Order'
		ordering = ['-created']

	def __str__(self):
		return str(self.id)


class OrderItem(models.Model):
	code = models.IntegerField(blank=True, null=True)
	product = models.CharField(max_length=250)
	quantity = models.IntegerField()
	price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='GBP Price')
	order = models.ForeignKey(Order, on_delete=models.CASCADE)

	class Meta:
		db_table = 'OrderItem'

	def sub_total(self):
		return self.quantity * self.price

	def __str__(self):
		return self.product