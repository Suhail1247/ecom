from django.urls import path
from . import views
app_name='ecomapp'
urlpatterns = [
    path('', views.allprocat,name='allprocat'),
    path('<slug:c_slug>/',views.allprocat,name='productsbycat'),
    path('<slug:c_slug>/<slug:p_slug>/',views.pdetails,name='pdetails')

]