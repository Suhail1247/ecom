from .models import Cart,CartItem
from .views import cart_id
def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cart_id=cart_id(request))
            cart_item=CartItem.objects.all().filter(cart=cart[:1])
            for ci in cart_item:
                item_count+=ci.qty
        except Cart.DoesNotExist:
            item_count=0
    return dict(item_count=item_count)