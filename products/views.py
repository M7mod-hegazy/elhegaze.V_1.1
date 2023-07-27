from multiprocessing import context
from os import name
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from datetime import datetime
from .models import Child, Product
from orders.models import Order, OrderDetails
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from accounts.models import UserProfile
from django.contrib.postgres.search import SearchVector
import qrcode
from io import BytesIO
from PIL import Image


# Import Pagination Stuff
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


def products(request):
    context = {
        'products': Product.objects.all()

    }
    if request.user.is_authenticated and not request.user.is_anonymous:
        if Order.objects.all().filter(user=request.user, is_finished=False):
            order = Order.objects.get(user=request.user, is_finished=False)
            orderdetails = OrderDetails.objects.all().filter(order=order)
            prototal = 0
            for prosup in orderdetails:
                prototal += prosup.quantity
            context = {
                'order': order,
                'prototal': prototal,
                'products': Product.objects.all()
            }
    return render(request, 'products/products.html', context)


def pro_child(request, pro_id):
    chil = Child.objects.all().filter(product__pk=pro_id)
    pchild = get_object_or_404(Product, pk=pro_id)
    product = Product.objects.all().prefetch_related('childs')
    p = Paginator(chil, 12)
    page = request.GET.get('page')
    prol = p.get_page(page)
    nums = "a" * prol.paginator.num_pages
    prochild = {
        'pchild': get_object_or_404(Product, pk=pro_id),
        'products': Product.objects.all(),
        'chil': Child.objects.all(),
        'prol': prol,
        'nums': nums

    }
    if request.user.is_authenticated and not request.user.is_anonymous:
        if Order.objects.all().filter(user=request.user, is_finished=False):
            order = Order.objects.get(user=request.user, is_finished=False)
            orderdetails = OrderDetails.objects.all().filter(order=order)
            prototal = 0
            for prosup in orderdetails:
                prototal += prosup.quantity
            prochild = {
                'order': order,
                'prototal': prototal,
                'products': Product.objects.all(),
                'pchild': get_object_or_404(Product, pk=pro_id),
                'products': Product.objects.all(),
                'chil': Child.objects.all(),
                'prol': prol,
                'nums': nums
            }

    return render(request, 'products/pro_child.html',  prochild)



def product_info(request, pro_id, chi_id):
    pchild = get_object_or_404(Child, product__pk=pro_id, pk=chi_id)
    pro5 = Product.objects.all()
    if request.user.is_authenticated and not request.user.is_anonymous:
        userprofile = UserProfile.objects.get(user=request.user)
        if Order.objects.all().filter(user=request.user, is_finished=False):
            order = Order.objects.get(user=request.user, is_finished=False)
            orderdetails = OrderDetails.objects.all().filter(order=order)
            prototal = 0
            for prosup in orderdetails:
                prototal += prosup.quantity
            return render(request, 'products/product_info.html', context={
                'pchild': pchild,
                'userprofile': userprofile,
                'order': order,
                'prototal': prototal,
                'products': pro5,
            })
        else:
            return render(request, 'products/product_info.html', context={
                'pchild': pchild,'products': pro5,
            })
    else:
        return render(request, 'products/product_info.html', context={
            'pchild': pchild,'products': pro5,
        })



def search_result(request):
    pro2 = Child.objects.all()
    pro5 = Product.objects.all()
    name = None
    code = None
    details = None
    seens = None
    p = None
    page = None
    prol=  None

    search_vector = SearchVector('name', 'code', 'details')
    if ('searchname' in request.GET) and request.GET['searchname'].strip():
        query_string = request.GET.get('searchname')
        seens = Child.objects.annotate(search=search_vector).filter(search=query_string)
        page = request.GET.get('page')
        paginator = Paginator(seens,12)
        try:  
            p = paginator.page(page)
        except PageNotAnInteger:
            p = paginator.page(1)
        except EmptyPage:
            p = paginator.page(paginator.num_pages)
        prol = seens.count()
        
  
        context3 = {
            'name': name,
            'code': code,
            'details':details,
            'products2': pro2,
            'products': pro5,
            'prol': prol,
            'p':p,
            'seens': seens, 'query_string': query_string
        }
    else:   
          context3 = {
            'name': name,
            'code': code,
            'details':details,
            'products2': pro2,
            'products': pro5,
           
        } 
        
    if request.user.is_authenticated and not request.user.is_anonymous:
        if Order.objects.all().filter(user=request.user, is_finished=False):
            order = Order.objects.get(user=request.user, is_finished=False)
            orderdetails = OrderDetails.objects.all().filter(order=order)
            prototal = 0
            for prosup in orderdetails:
                prototal += prosup.quantity
            context3 = {
                'order': order,
                'prototal': prototal,
                'name': name,
                'code': code,
                'details': details,
                'products2': pro2,
                'products': pro5,
                'prol': prol,
                'seens': seens,
                'query_string': query_string
            }
    return render(request, 'products/search_result.html', context3)


def search(request):
    pchild = {

        'products': Product.objects.all(),
    }

    return render(request, 'products/search.html', pchild)


# View for generating the QR code
def generate_qr_code(request, pro_id, chi_id):
    # Construct the complete URL using the request object and the ID
    current_url = request.build_absolute_uri()
    complete_url = f"{current_url}"

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(complete_url)
    qr.make(fit=True)

    # Create an image from the QR code data
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a BytesIO buffer to return it as a response
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response



