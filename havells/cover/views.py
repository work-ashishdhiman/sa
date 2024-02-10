from django.shortcuts import render
from django.views import View
from .models import Category
# Create your views here.

def home(request):
    return render(request,"app/home.html")

class CategoryView(View):
    def get(self,request,val):
        products = Category.objects.filter(category=val)
        # categoryid=Category.objects.filter(val=val)
        return render(request,"app/category.html",locals())