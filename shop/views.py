from django.shortcuts import render
from django.views import View

# Create your views here.
def home(request):
    return render(request, "shop/home.html")

class categoryView(View):
    def get(self, request, val):
        return render(request, "shop/category.html", locals())    