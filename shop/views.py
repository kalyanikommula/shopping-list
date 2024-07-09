from django.shortcuts import render
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
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, "shop/profile.html", locals()) 
        
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            county = form.cleaned_data['county']
            postcode = form.cleaned_data['postcode']

            reg = Customer(user=user,locality=locality,city=city,mobile=mobile,county=county,postcode=postcode)
            reg.save
            messages.success(request, "congradulations!! profile save successfully")
        else:
            messages.warning(request, "Invalid! input data")    

        return render(request, "shop/profile.html", locals()) 

   
