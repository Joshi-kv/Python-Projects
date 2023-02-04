from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from . models import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.db.models import Q


# Create your views here.
def home(request,c_slug=None):
    c_page=None
    products=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products=Product.objects.all().filter(category=c_page,availability=True)
    else:
        products=Product.objects.all().filter(availability=True)
        
        
    #paginator
    paginator=Paginator(products,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pdt=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pdt=paginator.page(paginator.num_pages)
    return render(request,'index.html',{'category':c_page,'product':pdt})


def product_detail(request,cat_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=cat_slug,slug=product_slug)
    except Exception as err:
        raise err
    return render(request,'product.html',{'product':product})


#search function
def search(request):
    product=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        product=Product.objects.all().filter(Q(name__icontains=query)|Q(description__icontains=query))
        return render(request,'search.html',dict(query=query,product=product))
