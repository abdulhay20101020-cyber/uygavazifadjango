from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'shop/index.html', {
        'categories': categories,
        'products': products
    })


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'shop/category.html', {
        'category': category,
        'products': products,
        'categories': categories
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    images = product.images.all()
    return render(request, 'shop/detail.html', {
        'product': product,
        'images': images
    })