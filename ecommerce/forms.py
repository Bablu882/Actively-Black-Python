from management.models import Profile
from django import forms
from .models import Add_Product
class  Product_forms(forms.ModelForm):
    # product_vender=forms.InlineForeignKeyField(profile=request.user)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        self.fields["product_name"].widget.attrs.update({
            'name':'product_name',
            'id':'product_name',
            'style':'height:40px',
            'size':'50px',
            'type':'text',
            'class':'form-control',
            'placeholder':'product_name',
            'maxlength':'50',
            'minlength':'6'
        })
        self.fields["product_description"].widget.attrs.update({
            'name':'product_description',
            'id':'product_description',
            'style':'height:150px',
            'size':'50px',
            'type':'text',
            'class':'form-control',
            'placeholder':'product_description',
            'maxlength':'50',
            'minlength':'6'
        })
        
        self.fields["product_image"].widget.attrs.update({
            'name':'product_image',
            'id':'product_image',
            'style':'height:40px',
            'size':'50px',
            'type':'text',
            'class':'form-control',
            'placeholder':'product_image',
            'maxlength':'50',
            'minlength':'6'
        })
        self.fields["product_catagory"].widget.attrs.update({
            'name':'product_catagory',
            'id':'product_catagory',
            'style':'height:40px',
            # 'size':'50px',
            'type':'text',
            'class':'form-control',
            'placeholder':'product_catagory',
            'maxlength':'50',
            'minlength':'6'
        })
        self.fields["product_price"].widget.attrs.update({
            'name':'product_price',
            'id':'product_price',
            'style':'height:40px',
            'size':'50px',
            'type':'text',
            'class':'form-control',
            'placeholder':'product_price',
            'maxlength':'50',
            'minlength':'6'
        })
        self.fields["product_discount"].widget.attrs.update({
            'name':'product_discount',
            'id':'product_discount',
            'style':'height:40px',
            'size':'50px',
            'type':'text',
            'class':'form-control',
            'placeholder':'product_discount',
            'maxlength':'50',
            'minlength':'6'
        })
        self.fields["additional_image1"].widget.attrs.update({
            'name':'additional_image1',
            'id':'product_description',
            'style':'height:40px',
            'size':'50px',
            'type':'text',
            'class':'form-control',
            'placeholder':'additional_image1',
            'maxlength':'50',
            'minlength':'6'
        })
        self.fields["additional_image2"].widget.attrs.update({
            'name':'additional_image2',
            'id':'additional_image2',
            'style':'height:40px',
            'size':'50px',
            'type':'text',
            'class':'form-control',
            'placeholder':'additional_image2',
            'maxlength':'50',
            'minlength':'6'
        })
        self.fields["additional_image3"].widget.attrs.update({
            'name':'additional_image3',
            'id':'additional_image3',
            'style':'height:40px',
            'size':'50px',
            'type':'text',
            'class':'form-control',
            'placeholder':'additional_image3',
            'maxlength':'50',
            'minlength':'6'
        })
        self.fields["product_height"].widget.attrs.update({
            'name':'product_height',
            'id':'product_height',
            'style':'height:40px',
            'size':'50px',
            'type':'text',
            'class':'form-control',
            'placeholder':'product_height',
            'maxlength':'50',
            'minlength':'6'
        })
        self.fields["product_width"].widget.attrs.update({
            'name':'product_width',
            'id':'product_width',
            'style':'height:40px',
            'size':'50px',
            'type':'text',
            'class':'form-control',
            'placeholder':'product_width',
            'maxlength':'50',
            'minlength':'6'
        })
        self.fields["product_pieces"].widget.attrs.update({
            'name':'product_pieces',
            'id':'product_pieces',
            'style':'height:40px',
            'size':'50px',
            'type':'text',
            'class':'form-control',
            'placeholder':'product_pieces',
            'maxlength':'50',
            'minlength':'6'
        })
        self.fields["product_available"].widget.attrs.update({
            'name':'product_available',
            'id':'product_available',
            'style':'height:40px',
            'size':'50px',
            'type':'text',
            'class':'form-control',
            'placeholder':'product_available',
            'maxlength':'50',
            'minlength':'6'
        })
        # self.fields["product_is_sale"].widget.attrs.update({
        #     'name':'product_is_sale',
        #     'id':'product_is_sale',
        #     'style':'height:40px',
        #     'size':'50px',
        #     'type':'text',
        #     'class':'form-control',
        #     'placeholder':'product_is_sale',
        #     'maxlength':'50',
        #     'minlength':'6'
        # })
        # self.fields["product_is_active"].widget.attrs.update({
        #     'name':'product_is_active',
        #     'id':'product_is_active',
        #     'style':'height:40px',
        #     'size':'50px',
        #     'type':'text',
        #     'class':'form-control',
        #     'placeholder':'product_is_active',
        #     'maxlength':'50',
        #     'minlength':'6'
        # })
        # self.fields["product_is_deleted"].widget.attrs.update({
        #     'name':'product_is_deleted',
        #     'id':'product_is_deleted',
        #     'style':'height:40px',
        #     'size':'50px',
        #     'type':'text',
        #     'class':'form-control',
        #     'placeholder':'product_is_deleted',
        #     'maxlength':'50',
        #     'minlength':'6'
        # })
        self.fields["product_slug"].widget.attrs.update({
            'name':'product_slug',
            'id':'product_slug',
            'style':'height:40px',
            'size':'50px',
            'type':'text',
            'class':'form-control',
            'placeholder':'product_slug',
            'maxlength':'50',
            'minlength':'6'
        })
        self.fields["product_weight"].widget.attrs.update({
            'name':'product_weight',
            'id':'product_weight',
            'style':'height:40px',
            'size':'50px',
            'type':'text',
            'class':'form-control',
            'placeholder':'product_weight',
            'maxlength':'50',
            'minlength':'6'
        })
    class Meta:
        model=Add_Product
        fields=['product_name','product_description','product_image','product_catagory','product_price','product_discount','additional_image1',
        'additional_image2','additional_image3','product_width','product_height','product_weight','product_pieces',
        'product_available','product_is_sale','product_is_active','product_is_deleted','product_slug','product_vender']