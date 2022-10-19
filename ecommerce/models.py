from django.db import models
from traitlets import default
from management.models import User
from management.models import Profile
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator



class Product_catagory(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True,verbose_name=_("Catagory Name"))
    image=models.ImageField(blank=True,null=True,upload_to='ecommerce/catagory-image',verbose_name=_("Catagory Image"))
    catagory_slug=models.SlugField(blank=True,null=True,allow_unicode=True,unique=True,verbose_name=_("Cat slugify"))

    
    def save(self,*args,**kwargs):
        self.catagory_slug=slugify(self.name)
        super().save(*args,**kwargs)


class Add_Product(models.Model):
    product_vender=models.ForeignKey(Profile,on_delete=models.CASCADE,verbose_name=_("product_vender"),blank=True,null=True)
    product_name=models.CharField(max_length=200,blank=True,null=True,verbose_name=_("Name"))
    product_description=models.TextField(verbose_name=_("Short Description"))
    product_image=models.ImageField(upload_to='ecommerce/product-image',default='ecommerce/default.jpg',verbose_name=_("Product Image"))
    product_catagory=models.ForeignKey(Product_catagory,on_delete=models.SET_NULL,blank=True,null=True,verbose_name=_("Catagory"))
    product_price=models.FloatField(blank=True,null=True,verbose_name=_("Price"))
    product_discount=models.FloatField(blank=True,null=True,verbose_name=_("Discount"))
    additional_image1=models.ImageField(blank=True,null=True,upload_to='ecommerce/additional-image',verbose_name=_("Additional Image1"))
    additional_image2=models.ImageField(blank=True,null=True,upload_to='ecommerce/additional-image',verbose_name=_("Additional Image2"))
    additional_image3=models.ImageField(blank=True,null=True,upload_to='ecommerce/additional-image',verbose_name=_("Additional Image3"))
    feedback_average=models.PositiveIntegerField(blank=True,null=True,verbose_name=_("Feedback Average"))
    feedback_number=models.PositiveIntegerField(blank=True,null=True,verbose_name=_("Feedback Number"))
    product_width=models.FloatField(blank=True,null=True,verbose_name=_("Width"))
    product_height=models.FloatField(blank=True,null=True,verbose_name=_("Height"))
    product_weight=models.FloatField(blank=True,null=True,verbose_name=_("Weight"))
    product_pieces=models.PositiveIntegerField(blank=True,null=True,verbose_name=_("Pieces/set"))
    product_available=models.PositiveIntegerField(blank=True,null=True,verbose_name=_("available"))
    product_is_sale=models.BooleanField(default=False,verbose_name=_("Sale"))
    product_is_active=models.BooleanField(default=False,verbose_name=_("Product active"))
    product_is_deleted=models.BooleanField(default=False,verbose_name=_("Product Deleted"))
    product_slug=models.SlugField(max_length=100,blank=True,null=True,allow_unicode=True,unique=True,verbose_name=_("Slugify"))
    date_upload=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name=_("-Date"))
    date_update=models.DateTimeField(auto_now=True,blank=True,null=True,verbose_name=_("-Update"))
    def __str__(self):
        return self.product_name

    def save(self,*args,**kwargs):
        self.product_slug=slugify(self.product_name)
        super().save(*args,**kwargs)    






class Product_rating(models.Model):
    related_product=models.ForeignKey(Add_Product,on_delete=models.CASCADE,
    blank=True,null=True,verbose_name=_("Add_product"))
    vendor=models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True,
    related_name='vender',verbose_name=_("Supplier"),)
    rate=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)],blank=True,null=True)
    clint_name=models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True,related_name='Customer',
    verbose_name=_("Clint"))
    clint_comment=models.CharField(max_length=500,blank=True,null=True,verbose_name=_("Comment"))
    active=models.BooleanField(default=True)
    rating_date=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    rating_update=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.related_product

