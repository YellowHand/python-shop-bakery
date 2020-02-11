from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Client,Product,ListProduct
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.decorators import login_required



#Category view
@login_required()
def allProdCat(request, c_slug=None):
	c_page = None
	products_list = None
	if c_slug!=None:
		c_page = get_object_or_404(Client,slug=c_slug)
		products_list = Product.objects.order_by('product__category','stock').filter(client=c_page,product__available=True,user_id=request.user.id)
	else:
		products_list = Product.objects.all().order_by('product__category','stock').filter(product__available=True,user_id=request.user.id)
	'''Pagination code'''
	paginator = Paginator(products_list, 100)
	try:
		page = int(request.GET.get('page','1'))
	except:
		page = 1
	try:
		products = paginator.page(page)
	except (EmptyPage,InvalidPage):
		products = paginator.page(paginator.num_pages)
	return render(request,'shop/category.html',{'client':c_page,'products':products})

@login_required()
def ProdCatDetail(request,c_slug,product_slug):
	try:
		product = Product.objects.get(client__slug=c_slug,slug=product_slug)
	except Exception as e:
		raise e
	return render(request,'shop/product.html', {'product':product})