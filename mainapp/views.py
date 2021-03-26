from django.shortcuts import render
from mainapp.models import ProductCategory, Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index(request):
    return render(request, 'mainapp/index.html')


# class ProductsView(ListView):
#     model = Product
#     template_name = 'mainapp/products.html'
#
#     def get_paginator():
#         queryset = Product.objects.all
#         per_page = 3
#         return paginator(queryset, per_page)


def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    per_page = 3
    if (len(products) <= per_page):
        show_pages = False
    else:
        show_pages = True
    paginator = Paginator(products.order_by('price'), per_page)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(page)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context = {'categories': ProductCategory.objects.all(), 'products': products_paginator, 'show_pages': show_pages}
    return render(request, 'mainapp/products.html', context)
