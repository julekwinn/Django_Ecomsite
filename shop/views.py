from django.shortcuts import render
from .models import Products

# Create your views here.

def index(request):
    products_objects = Products.objects.all()

    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        products_objects = products_objects.filter(title__icontains=item_name)

    return render(request,'shop/index.html',{'products_objects': products_objects})
