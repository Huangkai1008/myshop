from django.shortcuts import render, get_object_or_404
from .models import Category, Product
# Create your views here.


def product_list(request, category_slug=None):
    """
    列出所有产品或者是给出后的筛选后的产品
    :param request:
    :param category_slug:
    :return:
    """
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    """
    检索和展示单一的产品
    :param request:
    :param id:
    :param slug:
    :return:
    """
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})