from django.shortcuts import render, get_object_or_404
from .models import category, product
from django.core.paginator import Paginator,InvalidPage,EmptyPage


def allprocat(request, c_slug=None):
    cpage = None
    products = None
    if c_slug is not None:
        cpage = get_object_or_404(category, slug=c_slug)
        products = product.objects.all().filter(category=cpage, available=True)
    else:
        products = product.objects.all().filter(available=True)
    paginator=Paginator(products,6)
    try:
        page=int(request.GET.get('page',1))
    except:
        page=1
    try:
        productss=paginator.page(page)
    except (EmptyPage,InvalidPage):
        productss=paginator.page(paginator.num_pages)
    return render(request, 'category.html', {'category': cpage, 'products': productss})
def pdetails(request,c_slug,p_slug):
    try:
        p=product.objects.get(category__slug=c_slug,slug=p_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':p})
