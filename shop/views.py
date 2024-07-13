from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.db.models import Count
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from . models import Product, Customer, Cart, Contact
from . forms import CustomerProfileForm



# Create your views here.
def home(request):
    return render(request, "shop/home.html")

def about(request):
    return render(request, "shop/about.html")

def contact(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.message=message
        contact.save()
        return redirect("success")
    return render(request, "shop/contact.html")


def success(request):
    return render(request, "shop/success.html")


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

@method_decorator(login_required, name='dispatch')
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

@login_required   
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

class deleteAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        add.delete()
        messages.success(request, "Address deleted successfully.")
        return redirect("profile")

@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get("prod_id")
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect("/cart")

@login_required
def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user) 
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = total = 5    
    return render(request, "shop/addtocart.html", locals())

def plus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 5
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }   
        return JsonResponse(data) 


def minus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 5
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }   
        return JsonResponse(data) 

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 5
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }   
        return JsonResponse(data) 

def placeorder(request):
    return render(request, "shop/placeorder.html")



def search(request):
    query = request.GET.get('search', '')
    print(f"Search query: {query}")  # Debugging: Print the search query

    product = Product.objects.filter(Q(title__icontains=query) | Q(category__icontains=query))
    return render(request,"shop/search.html", locals())


