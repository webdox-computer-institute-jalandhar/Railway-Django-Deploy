from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from core import settings
from .models import Product
from .forms import ProductForm

# List all Products
def product_list(request):
    products = Product.objects.all().order_by('-id')
    return render(request, 'products/product_list.html', {
        'products': products
    })

# Add Product
def add_product(request):
    form = ProductForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('product_list')

    return render(request, 'products/product_form.html', {
        'form': form,
        'title': 'Add Product'
    })

# Update Product
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    form = ProductForm(
        request.POST or None,
        request.FILES or None,
        instance=product
    )

    if form.is_valid():
        form.save()
        return redirect('product_list')

    return render(request, 'products/product_form.html', {
        'form': form,
        'title': 'Update Product'
    })

# Delete Product
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    return render(request, 'products/delete.html', {
        'product': product
    })

def test_media(request):
    return HttpResponse(settings.MEDIA_ROOT)