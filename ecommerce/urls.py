from django.urls import path
from .views import *

urlpatterns=[
    path('listing-product',listing_product,name='listing-product'),
    path('add-product',add_product,name='add-product'),
    path('shop',shop,name='shop'),
]