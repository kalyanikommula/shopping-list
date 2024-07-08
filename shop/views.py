from django.shortcuts import render
from django.views import View
from . models import Product

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