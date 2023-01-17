from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render
from cart.forms import ShippingForm
from django.core.mail import send_mail

from cart.models import Cart, Cartitem, Shipping
from shop.models import Product

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def CartPage(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = Cartitem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.product_price * cart_item.quantity)
            quantity += cart_item.quantity
        # tax = (2 * total)/100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        # 'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'cart.html', context)

def add_cart(request, id):
    product = Product.objects.get(id=id)
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    try:
        cart_item = Cartitem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except Cartitem.DoesNotExist:
        cart_item = Cartitem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    return redirect('Cart')

def remove_cart(request, id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product,id=id)
    cart_item = Cartitem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('Cart')

def remove_cart_item(request, id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product,id=id)
    cart_item = Cartitem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('Cart')

def CheckoutPage(request, total=0, quantity=0, cart_items=None):
    if request.method == "POST":
        fm = ShippingForm(request.POST)
        if fm.is_valid():
            fnm = fm.cleaned_data['f_name']
            lnm = fm.cleaned_data['l_name']
            add = fm.cleaned_data['address']
            city = fm.cleaned_data['city']
            st = fm.cleaned_data['state']
            zip = fm.cleaned_data['zipcode']
            eml = fm.cleaned_data['email']
            cnt = fm.cleaned_data['contact']
            reg = Shipping(f_name=fnm, l_name=lnm, address=add, city=city, state=st, zipcode=zip, email=eml, contact=cnt)
            reg.save()

            tax = 0
            grand_total = 0
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = Cartitem.objects.filter(cart=cart, is_active=True)
            for cart_item in cart_items:
                total += (cart_item.product.product_price * cart_item.quantity)
                quantity += cart_item.quantity
            # tax = (2 * total)/100
            grand_total = total + tax
            subject = "Order Reciept"
            to_email = ['livingdreams.mumbai@gmail.com', eml]
            items = []
            for i in cart_items:
                items += i.product.product_name
            
            send_mail(
            subject,
            'Email: ' + eml + '\nTo ' + fnm + ' ' + lnm + ',\nShipping Address,\n' + add + '\n' + city + ' ,' + st + '\nZip Code: ' + str(zip) + '\nContact no: ' + str(cnt) +
            '\nItems: ' + ''.join(items) + '\nGrand Total: ₹' + str(grand_total),
            eml,
            to_email,
            )
            return redirect('Thankyou')
            
    else:
        fm = ShippingForm()

    try:
        tax = 0
        grand_total = 0
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = Cartitem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.product_price * cart_item.quantity)
            quantity += cart_item.quantity
        # tax = (2 * total)/100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass

    context = {
        "form": fm,
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        # 'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'checkout.html', context)

def ThankyouPage(request):
    cart_item = Cartitem.objects.all()
    cart_item.delete()
    return render(request, 'thankyou.html')