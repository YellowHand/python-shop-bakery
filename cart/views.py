from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from orders.models import Order, OrderItem
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required()
def _cart_id(request):
  cart = request.session.session_key
  if not cart:
      cart = request.session.create()
  return cart

@login_required()
def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
                cart_id = _cart_id(request)
            )
        cart.save()
    try:
      cart_item = CartItem.objects.get(product=product, cart=cart)
      if cart_item.quantity < cart_item.product.stock:
        if request.method == 'POST':
          quantity = request.POST['quantity']
          cart_item.quantity += int(quantity)
      cart_item.save()
    except CartItem.DoesNotExist:
      cart_item = CartItem.objects.create(
                  product = product,
                  quantity = request.POST['quantity'],
                  cart = cart
          )
      cart_item.save()
    return redirect('cart:cart_detail')

@login_required()
def cart_detail(request, total=0, counter=0, cart_items = None):
  try:
      cart = Cart.objects.get(cart_id=_cart_id(request))
      cart_items = CartItem.objects.filter(cart=cart, active=True)
      for cart_item in cart_items:
          total += (cart_item.product.price * cart_item.quantity)
          counter += cart_item.quantity
  except ObjectDoesNotExist:
      pass
  if request.method == 'POST':
    customerNumber = request.POST['customerNumber']
    email = request.POST['email']
    address = request.POST['address']
    city = request.POST['city']
    postCode = request.POST['postCode']
    country = request.POST['country']
    shippingName = request.POST['shippingName']
    shippingAddress = request.POST['shippingAddress']
    shippingCity = request.POST['shippingCity']
    shippingPostcode = request.POST['shippingPostcode']
    shippingCountry = request.POST['shippingCountry']
    deliveryPhone = request.POST['deliveryPhone']
    phone = request.POST['phone']
    deliveryMonday = request.POST['deliveryMonday']
    deliveryTuesday = request.POST['deliveryTuesday']
    deliveryWednesday = request.POST['deliveryWednesday']
    deliveryThursday = request.POST['deliveryThursday']
    deliveryFriday = request.POST['deliveryFriday']
    deliverySaturday = request.POST['deliverySaturday']
    message = request.POST['message']


    order_details = Order.objects.create(total=total, customerNumber=customerNumber, address=address, city=city, postCode=postCode,country=country, shippingName=shippingName, shippingAddress=shippingAddress, shippingCity=shippingCity, shippingPostcode=shippingPostcode, shippingCountry=shippingCountry, deliveryPhone=deliveryPhone, phone=phone, email=email, deliveryMonday=deliveryMonday, deliveryTuesday=deliveryTuesday, deliveryWednesday=deliveryWednesday, deliveryThursday=deliveryThursday, deliveryFriday=deliveryFriday, deliverySaturday=deliverySaturday, message=message)
    order_details.save()
    for order_item in cart_items:
					oi = OrderItem.objects.create(
              code = order_item.product.product.code,
							product = order_item.product.product.name,
							quantity = order_item.quantity,
							price = order_item.product.price,
							order = order_details
						)
					oi.save()
					'''Delete stock'''
					products = Product.objects.get(id=order_item.product.id)
					products.stock = int(order_item.product.stock - order_item.quantity)
					products.save()
					order_item.delete()
					print('The order has been created')
    messages.success(request, 'You placed an order!')
    return redirect('shop:allProdCat')
  return render(request, 'cart/cart.html', dict(cart_items = cart_items, total = total, counter = counter))

@login_required()
def cart_remove(request, product_id):
	cart = Cart.objects.get(cart_id=_cart_id(request))
	product = get_object_or_404(Product, id=product_id)
	cart_item = CartItem.objects.get(product=product, cart=cart)
	if cart_item.quantity > 1:
		cart_item.quantity -= 1
		cart_item.save()
	else:
		cart_item.delete()
	return redirect('cart:cart_detail')

@login_required()
def full_remove(request, product_id):
	cart = Cart.objects.get(cart_id=_cart_id(request))
	product = get_object_or_404(Product, id=product_id)
	cart_item = CartItem.objects.get(product=product, cart=cart)
	cart_item.delete()
	return redirect('cart:cart_detail')