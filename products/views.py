from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
  """ 
  Shows all products, includes sorting and listing
  """
  products = Product.objects.all()
  
  context = {
    'products': products,
  }
  
  return render(request, 'products/products.html', context)
