from django.urls import path
from . import views
from .views import *


urlpatterns=[
    path("category-list/", views.category_list, name="category-list"),
    path('shop/', views.shop, name='shop'),
    path('shop/super/<str:slug>', views.super_category, name='super-category'),
    path('shop/main/<str:slug>', views.main_category, name='main-category'),
    path('shop/sub/<str:slug>', views.sub_category, name='sub-category'),
    path('shop-ajax/', views.CategoryJsonListView.as_view(),
         name='shop-ajax'),
    path('listing-product',listing_product,name='listing-product'),
    path('add-product',add_product,name='add-product'),
    # path('shop',shop,name='shop'),
]