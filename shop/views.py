from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from . models import Product, Customer
from . forms import CustomerProfileForm

# Create your views here.
def home(request):
    return render(request, "shop/home.html")

def about(request):
    return render(request, "shop/about.html")

def contact(request):
    return render(request, "shop/contact.html")


class categoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, "shop/category.html", locals())   


class categoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, "shop/category.html", locals())   


class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)

        return render(request, "shop/productdetail.html", locals()) 


class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, "shop/profile.html", locals()) 
        
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            county = form.cleaned_data['county']
            postcode = form.cleaned_data['postcode']

            reg = Customer(user=user,name=name,locality=locality,city=city,mobile=mobile,county=county,postcode=postcode)
            reg.save()
            messages.success(request, "congradulations!! profile save successfully")
        else:
            messages.warning(request, "Invalid! input data")    

        return render(request, "shop/profile.html", locals()) 

   
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, "shop/address.html", locals())

class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, "shop/updateAddress.html", locals())   
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.county = form.cleaned_data['county']
            add.postcode = form.cleaned_data['postcode']
            add.save()
            messages.success(request, "congratulations! profile update successfully")
        else:
            messages.warning(request, "Invalid input data") 
        return redirect("address")      

        return render(request, "shop/updateAddress.html", locals())

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get("prod_id")
    product = Product.objects.get(id=product_id)
    cart(user=user,product=product).save()
    return redirect("/cart")
 
def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user) 
    return render(request, "shop/addtocart.html", locals())
