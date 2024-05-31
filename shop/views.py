from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    products_objects = Products.objects.all()

# search code

    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        products_objects = products_objects.filter(title__icontains=item_name)


# paginator code

    paginator = Paginator(products_objects, 4)
    page = request.GET.get('page')
    products_objects = paginator.get_page(page)


    return render(request,'shop/index.html',{'products_objects': products_objects})


def detail(request,id):
    product_object = Products.objects.get(id=id)

    return render(request, 'shop/detail.html', {'product_object':product_object})
