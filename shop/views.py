import imp
from django.shortcuts import render
from .models import Order, product
from django.http import HttpResponse
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    products_object = product.objects.all()

    # search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name != None:
        products_object = product.objects.filter(title__icontains=item_name)


    # pagination code
    paginator = Paginator(products_object,4)
    page = request.GET.get('page')
    products_object = paginator.get_page(page)


    return render(request,'shop/index.html',{'products_object':products_object})


def detail(request,id):
    product_id = product.objects.get(id=id)
    return render(request,'shop/detail.html',{'product_id':product_id})



# chechout

def checkout(request):

    if request.method == 'POST':
        items = request.POST.get('items',"")
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")
        order = Order(items=items,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,total=total)

        order.save()

    return render(request,'shop/checkout.html')