from django.shortcuts import render, redirect, get_object_or_404
from ecomapp.models import product
from .models import Cart,CartItem
from django.core.exceptions import ObjectDoesNotExist

def cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart
def add_cart(request,product_id):
    p=product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=cart_id(request))
        cart.save(),
    try:
        cart_item=CartItem.objects.get(p=p,cart=cart)
        if cart_item.qty < cart_item.p.stock:
            cart_item.qty +=1
        cart_item.save(),
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(p=p,qty=1,cart=cart)
        cart_item.save()
    return redirect('cart:cart_detail')
def cart_detail(request,total=0,counter=0,cart_item=None):
    try:
        cart=Cart.objects.get(cart_id=cart_id(request))
        cart_item=CartItem.objects.all()
        for ci in cart_item:
            total+=(ci.p.price*ci.qty)
            counter+=ci.qty
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_item=cart_item,total=total,counter=counter))

def minus(request,product_id):
    cart=Cart.objects.get(cart_id=cart_id(request))
    p=get_object_or_404(product,id=product_id)
    cart_item=CartItem.objects.get(p=p,cart=cart)
    if cart_item.qty > 1:
        cart_item.qty -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')
def trash(request,product_id):
    cart=Cart.objects.get(cart_id=cart_id(request))
    p=get_object_or_404(product,id=product_id)
    cart_item=CartItem.objects.get(p=p,cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')