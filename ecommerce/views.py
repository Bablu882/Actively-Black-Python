from email import message
from typing import List
from django.shortcuts import redirect, render
from management.models import User,Profile
from .models import Add_Product,Product_catagory
from .forms import *
from django.contrib import messages
# Create your views here

def listing_product(request):
    products=list(Add_Product.objects.all().filter(product_vender=request.user.profile))
    return render(request,'ecommerce/listing-product.html',{'products':products})


def add_product(request):
    if request.method=='POST':
        form=Product_forms(request.POST,request.FILES)
        if form.is_valid():
            product=form.save(commit=False)
            product.product_vender=request.user.profile
            product.save()
            messages.success(request,'Product added succesfully !')
            form=Product_forms()
            return redirect('/add-product')
    form=Product_forms()  
    return render(request,'ecommerce/add-product.html',{'form':form})


def shop(request):
    products=Add_Product.objects.all()
    return render(request,'ecommerce/shop.html',{'products':products})    