from django.shortcuts import render,redirect,get_object_or_404
from .models import Product

from .models import *
# Create your views here.

def store(request):
    if request.method == "POST":
         search = request.POST['search']
         products = Product.objects.all().order_by('-id').filter(name__startswith=search)
         context = {'products':products}
         return render(request, 'store/store.html', context)
    else:
        products = Product.objects.all().order_by('-id')
        context = {'products':products}
        return render(request, 'store/store.html', context)

def ProductDetail(request,todo_pk):
    todo = get_object_or_404(Product,pk=todo_pk)
    context = {'products':todo}
    return render(request, 'store/detail_product.html', context)

def cart(request):
    #if user is login
    if request.user.is_authenticated:
        #access one to one relation we have link customer with user
        customer = request.user.customer
        #the resean we did this way is because we want to either create the order or
        #get if exist
        #we either create or find it if we do that get get the item attached to that
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        #we are able to query child object by setting the parent value thn child objects
        #with all lowercase value then _set.all() this get all other item tha have parent order
        items = order.orderitem_set.all()
    else:
        #if user is not login
        items = []
        #we have the value of order but we never pass it in else statement
        #if user is not login we create manually it ourself
        order={'get_cart_total':0,'get_cart_items':0}

    context = {'items':items,'order':order}
    return render(request, 'store/cart.html', context)

def checkout(request):
        #if user is login
        if request.user.is_authenticated:
            #access one to one relation we have link customer with user
            customer = request.user.customer
            #the resean we did this way is because we want to either create the order or
            #get if exist
            #we either create or find it if we do that get get the item attached to that
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            #we are able to query child object by setting the parent value thn child objects
            #with all lowercase value then _set.all() this get all other item tha have parent order
            items = order.orderitem_set.all()
        else:
            #if user is not login
            items = []
            #we have the value of order but we never pass it in else statement
            #if user is not login we create manually it ourself
            order={'get_cart_total':0,'get_cart_items':0}

        context = {'items':items,'order':order}
        return render(request, 'store/checkout.html', context)
