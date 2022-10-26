from django.urls import path
from . import views
from .views import *

# app_name='ecommerce'
urlpatterns=[
    path("category-list/", views.category_list, name="category-list"),
    path('shop/', views.shop, name='shop'),
    path('shop/super/<str:slug>', views.super_category, name='super-category'),
    path('shop/main/<str:slug>', views.main_category, name='main-category'),
    path('shop/sub/<str:slug>', views.sub_category, name='sub-category'),
    path('shop-ajax/', views.CategoryJsonListView.as_view(), name='shop-ajax'),
    path('listing-product',listing_product,name='listing-product'),
    path('add-product',add_product,name='add-product'),
    path('edit-product/<slug:slug>',edit_product,name='edit-product'),
    path('home',home,name='home'),
    path('product-details/<slug:slug>',product_details,name='product-details'),
    path('rating/', views.product_rating, name="product_rating"),


    path('add_to_cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.cart, name='cart'),
    path('cart/<str:country>/', views.StatesJsonListView.as_view(), name="get-states"),
    path('order/remeve-product/<int:productdeatails_id>',
         views.remove_item, name="remove-item"),
    path('payment/', views.payment, name="payment"),
    path('payment_blance/', views.payment_blance, name="payment-blance"),
    path('payment_cash/', views.payment_cash, name="payment-cash"),
    path('order/cancel/', views.CancelView.as_view(), name='cancel'),
    path('order/success/', views.success, name='success'),
    path('create_checkout_session/',
         views.create_checkout_session, name='create_checkout_session'),
    path('orders/webhook/', views.my_webhook_view, name='my-webhook'),
    path('verify-payment/', views.verify_payment_razorpay, name="verify-payment"),
    path('checkout-paymob/<int:id>',
         views.checkout_payment_paymob, name="checkout-paymob"),
    path('api/callbacks/', views.my_webhook_view_paymob,
         name="webhook-view-paymob"),
    path('set_currency/', views.set_currency , name='set-currency'),
     

    path('carted',cart_add,name='carted')     

]