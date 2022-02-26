from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('account/',views.account,name='account'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('contact/',views.contact,name='contact'),
    path('service/',views.service,name='service'),
    path('shop/',views.shop,name='shop'),
    path('shopdetail/',views.shopdetail,name='shopdetail'),
    path('wishlist/',views.wishlist,name='wishlist')
]
