from django.shortcuts import render
from ecomapp.models import product
from django.db.models import Q


def searchprod(request):
    p = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        p = product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
        return render(request, 'search.html', {'product': p,'query':query})
