from django.db import models
from django.urls import reverse
from django.conf import settings

class Client(models.Model):
	name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	slug = models.SlugField(max_length=250, unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'client'
		verbose_name_plural = 'clients'

	def get_url(self):
		return reverse('shop:products_by_clients', args=[self.slug])

	def __str__(self):
		return '{}'.format(self.name)

class ListProduct(models.Model):
	name = models.CharField(max_length=250, unique=False)
	code = models.IntegerField(blank=True, null=True)
	category = models.CharField(max_length=250, unique=False)
	description = models.TextField(blank=True)
	weight = models.IntegerField()
	image = models.ImageField(upload_to='images/%Y/%m/%d/%H/%m/%s/')
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


	def __str__(self):
	 return '{}'.format(self.name)

class Product(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	product = models.ForeignKey(ListProduct, on_delete=models.CASCADE)
	slug = models.SlugField(max_length=250, unique=False)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	stock = models.IntegerField(default=2000000000)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('user',)
		verbose_name = 'product'
		verbose_name_plural = 'products'

	def get_url(self):
		return reverse('shop:ProdCatDetail', args=[self.client.slug, self.slug])

	def __str__(self):
		return '{}'.format(self.user)
