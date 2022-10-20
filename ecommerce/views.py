from django.shortcuts import redirect, render,get_object_or_404
from management.models import User,Profile
# from .models import Add_Product,Product_catagory
from .forms import *
from django.contrib import messages
from .models import SubCategory,MainCategory,MiniCategory,SuperCategory
from django.views.generic import View
from django.http import JsonResponse
from .models import Product,ProductRating
from django.db.models import Sum
# Create your views here

def listing_product(request):
    products=list(Product.objects.all().filter(product_vendor=request.user.profile))
    return render(request,'ecommerce/listing-product.html',{'products':products})


def add_product(request):
    if request.method=='POST':
        form=Product_forms(request.POST,request.FILES)
        if form.is_valid():
            product=form.save(commit=False)
            product.product_vendor=request.user.profile
            product.save()
            messages.success(request,'Product added succesfully !')
            form=Product_forms()
            return redirect('/add-product')
    form=Product_forms()  
    return render(request,'ecommerce/add-product.html',{'form':form})


def home(request):
    products=Product.objects.all()
    return render(request,'ecommerce/shop.html',{'products':products})    

def shop(request):

    return render(request, "ecommerce/shop-grid-left.html")


def super_category(request, slug):

    super_category_obj = SuperCategory.objects.get(slug=slug)
    main_category_obj = MainCategory.objects.all().filter(
        super_category=super_category_obj)

    context = {
        "main_category_obj": main_category_obj,
        "super_category_obj": super_category_obj,
        "slug": slug,

    }
    return render(request, "ecommerce/shop-super-category.html", context)


def main_category(request, slug):

    main_category_obj = MainCategory.objects.get(slug=slug)
    sub_category_obj = SubCategory.objects.all().filter(
        main_category=main_category_obj)

    context = {
        "sub_category_obj": sub_category_obj,
        "main_category_obj": main_category_obj,
        "slug": slug,
    }
    return render(request, "ecommerce/shop-main-category.html", context)


def sub_category(request, slug):

    sub_category_obj = SubCategory.objects.get(slug=slug)
    mini_category_obj = MiniCategory.objects.all().filter(
        sub_category=sub_category_obj)

    context = {
        "mini_category_obj": mini_category_obj,
        "sub_category_obj": sub_category_obj,
        "slug": slug,
    }
    return render(request, "ecommerce/shop-sub-category.html", context)


def category_list(request):
    supercategory = SuperCategory.objects.all()
    maincategory = MainCategory.objects.all()
    subcategory = SubCategory.objects.all()
    minicategory = MiniCategory.objects.all()
    context = {
        'supercategory': supercategory,
        'maincategory': maincategory,
        'subcategory': subcategory,
        'minicategory': minicategory,
    }

    return render(request, "ecommerce/category-list.html", context)


class CategoryJsonListView(View):
    def get(self, *args, **kwargs):

        upper = int(self.request.GET.get("num_products"))
        orderd_by = self.request.GET.get("order_by")
        CAT_id = self.request.GET.get("CAT_id")
        CAT_type = self.request.GET.get("cat_type")

        if CAT_type == "all":
            lower = upper - 10
            # print(lower, upper)
            products = list(
                Product.objects.all().filter(PRDISDeleted = False , PRDISactive = True ).values().order_by(orderd_by)[lower:upper])
            products_size = len(Product.objects.all().filter(PRDISDeleted = False , PRDISactive = True ))
            max_size = True if upper >= products_size else False
            return JsonResponse({"data": products,  "max": max_size, "products_size": products_size, }, safe=False)

        else:      # 3
            lower = upper - 10
            # print(lower, upper)
            if CAT_type == "super":

                products = list(
                    Product.objects.all().filter(product_supercategory=int(CAT_id), PRDISDeleted = False , PRDISactive = True ).values().order_by(orderd_by)[lower:upper])
                products_size = len(
                    Product.objects.all().filter(product_supercategory=int(CAT_id), PRDISDeleted = False , PRDISactive = True ))
            elif CAT_type == "main":
                products = list(
                    Product.objects.all().filter(product_maincategory=int(CAT_id), PRDISDeleted = False , PRDISactive = True ).values().order_by(orderd_by)[lower:upper])
                products_size = len(
                    Product.objects.all().filter(product_maincategory=int(CAT_id), PRDISDeleted = False , PRDISactive = True ))
            elif CAT_type == "sub":
                products = list(
                    Product.objects.all().filter(product_subcategory=int(CAT_id), PRDISDeleted = False , PRDISactive = True ).values().order_by(orderd_by)[lower:upper])
                products_size = len(
                    Product.objects.all().filter(product_subcategory=int(CAT_id), PRDISDeleted = False , PRDISactive = True ))

            else:
                products = list(
                    Product.objects.all().filter(product_minicategor=int(CAT_id), PRDISDeleted = False , PRDISactive = True ).values().order_by(orderd_by)[lower:upper])
                products_size = len(
                    Product.objects.all().filter(product_minicategor=int(CAT_id), PRDISDeleted = False , PRDISactive = True ))

            max_size = True if upper >= products_size else False
            return JsonResponse({"data": products, "max": max_size, "products_size": products_size, }, safe=False)


def product_details(request, slug):
    # if not request.session.has_key('currency'):
    #     request.session['currency'] = settings.DEFAULT_CURRENCY

    product_detail = get_object_or_404(Product, PRDSlug=slug, PRDISactive=True)
    # product_image = ProductImage.objects.all().filter(PRDIProduct=product_detail)
    related_products_minicategor = product_detail.product_minicategor
    related_products = Product.objects.all().filter(
        product_minicategor=related_products_minicategor, PRDISactive=True)
    supplier_Products = Product.objects.all().filter(product_vendor=product_detail.product_vendor,
                                                     product_minicategor=related_products_minicategor, PRDISactive=True)

    # related = ProductAlternative.objects.all().filter(PALNProduct=product_detail)
    # related_products = product_detail.alternative_products.all()

    product_feedback = ProductRating.objects.all().filter(
        PRDIProduct=product_detail, active=True)
    feedback_sum = ProductRating.objects.all().filter(
        PRDIProduct=product_detail, active=True).aggregate(Sum('rate'))
    feedbak_number = product_feedback.count()
    
    try:

        average_rating = int(feedback_sum["rate__sum"]) / feedbak_number

        start_1_sum =  ProductRating.objects.all().filter(
            PRDIProduct=product_detail, active=True , rate = 1).count()

        start_2_sum =  ProductRating.objects.all().filter(
            PRDIProduct=product_detail, active=True , rate = 2).count()

        start_3_sum =  ProductRating.objects.all().filter(
            PRDIProduct=product_detail, active=True , rate = 3).count()

        start_4_sum =  ProductRating.objects.all().filter(
            PRDIProduct=product_detail, active=True , rate = 4).count()
            
        start_5_sum =  ProductRating.objects.all().filter(
            PRDIProduct=product_detail, active=True , rate = 5).count()
        
        

        start_1 = (start_1_sum/ feedbak_number) * 100
        start_2 = (start_2_sum / feedbak_number) * 100
        start_3 = (start_3_sum / feedbak_number) * 100
        start_4 = (start_4_sum / feedbak_number) * 100
        start_5 = (start_5_sum / feedbak_number) * 100

    except:
        average_rating = 0
        start_1 = 0
        start_2 = 0
        start_3 = 0
        start_4 = 0
        start_5 = 0

    context = {
        'product_detail': product_detail,
        # 'product_image': product_image,
        'related_products': related_products,
        'supplier_Products': supplier_Products,
        # 'related_products': related_products,
        'product_feedback': product_feedback,
        'average_rating': average_rating,
        'feedbak_number': feedbak_number,
        "start_1":start_1,
        "start_2":start_2,
        "start_3":start_3,
        "start_4":start_4,
        "start_5":start_5,

    }
    return render(request, 'ecommerce/shop-product-details.html', context)