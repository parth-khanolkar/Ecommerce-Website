from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.core.mail import send_mail

from shop.models import Product
from django.db.models import Q

# Create your views here.
def HomePage(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def ShopPage(request):
    products = Product.objects.all()
    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()
    context = {
        'products': paged_products, 
        'product_count': product_count,
    }
    return render(request, 'shop.html', context)

def sort_desc(request):
    products = Product.objects.all().order_by('product_name')
    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()
    context = {
        'products': paged_products, 
        'product_count': product_count,
    }
    return render(request, 'shop.html', context)

def sort_asc(request):
    products = Product.objects.all().order_by('-product_name')
    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()
    context = {
        'products': paged_products, 
        'product_count': product_count,
    }
    return render(request, 'shop.html', context)

def sort_l_to_h(request):
    products = Product.objects.all().order_by('product_price')
    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()
    context = {
        'products': paged_products, 
        'product_count': product_count,
    }
    return render(request, 'shop.html', context)

def sort_h_to_l(request):
    products = Product.objects.all().order_by('-product_price')
    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()
    context = {
        'products': paged_products, 
        'product_count': product_count,
    }
    return render(request, 'shop.html', context)

def filter_LR(request):
    products = Product.objects.filter(Q(product_collection__icontains='LR'))
    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()
    context = {
        'products': paged_products, 
        'product_count': product_count,
    }
    return render(request, 'shop.html', context)

def filter_BR(request):
    products = Product.objects.filter(Q(product_collection__icontains='BR'))
    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()
    context = {
        'products': paged_products, 
        'product_count': product_count,
    }
    return render(request, 'shop.html', context)

def filter_K(request):
    products = Product.objects.filter(Q(product_collection__icontains='K'))
    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()
    context = {
        'products': paged_products, 
        'product_count': product_count,
    }
    return render(request, 'shop.html', context)

def NewArrivalsPage(request):
    products = Product.objects.filter(Q(product_collection__icontains='NA'))
    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()
    context = {
        'products': paged_products, 
        'product_count': product_count,
    }
    return render(request, 'newarrivals.html', context)

def CataloguePage(request):
    return render(request, 'catalogue.html')

def AboutPage(request):
    return render(request, 'about.html')

def ContactPage(request):
    if request.method == "POST":
        c_fname = request.POST['c_fname']
        c_lname = request.POST['c_lname']
        c_email = request.POST['c_email']
        c_subject = request.POST['c_subject']
        c_message = request.POST['c_message']

        send_mail(
            c_subject,
            'Email: ' + c_email + '\nFrom ' + c_fname + ' ' + c_lname + ',\n' + c_message,
            c_email,
            ['livingdreams.mumbai@gmail.com']
        )
        message = str(c_fname) + ", We have received your message and we will revert ASAP!"
        return render(request, 'contact.html', {'message': message})

    else:    
        return render(request, 'contact.html')

def DetailsPage(request, id):
    product = Product.objects.get(pk = id)
    items = Product.objects.all()
    return render(request, 'details.html', {'product': product, 'items': items})

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.filter(Q(product_desc__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
        context = {
            'products': products,
            'product_count': product_count
        }
    return render(request, 'shop.html', context)