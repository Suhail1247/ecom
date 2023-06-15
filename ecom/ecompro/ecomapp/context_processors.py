from .models import category
def menu(request):
    link=category.objects.all()
    return dict(link=link)