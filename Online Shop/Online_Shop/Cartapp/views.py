from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from Home.models import Product
from . models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
# to create session
def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

#function for add items to cart
def add_cart(request,product_id):
    product=Product.objects.get(id=product_id) #to fetch product id from db
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request)) #to fetch session from db
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=_cart_id(request))
        cart.save(),
    try:
        cart_item=CartItem.objects.get(product=product,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity+=1 #to add quantity of product
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('Cartapp:cart_detail')

# function to get cart detail
def cart_detail(request,total=0,counter=0,cart_items=None):
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart_items=CartItem.objects.filter(cart=cart,active=True)#to get added items from cart and show it in the page
        for cart_item in cart_items:
            total+=(cart_item.product.price * cart_item.quantity)#to sum the total price when item add
            counter+=cart_item.quantity #to count the total number of items in cart
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))

#function for decrease quantity
def remove_item(request,product_id):
    cart=Cart.objects.filter(cart_id=_cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item=CartItem.objects.get(product=product,cart=cart[:1])
    if cart_item.quantity > 1 :
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('Cartapp:cart_detail')

#function to delete items
def item_delete(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item=CartItem.objects.get(product=product,cart=cart)
    cart_item.delete()
    return redirect('Cartapp:cart_detail')
    