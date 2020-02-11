from django.shortcuts import render, get_object_or_404
from .models import AllProduct

def index(request):
  context = {
      'products': AllProduct.objects.order_by('category').filter(is_published=True)
  }
  return render(request, 'offers/products.html', context)


def product(request, product_id):
    product = get_object_or_404(AllProduct, pk=product_id)

    context = {
      'product': product,
    }
    return render(request, 'offers/product.html', context)


