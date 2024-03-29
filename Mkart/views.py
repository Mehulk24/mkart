from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from Mkart.models import (
    Ladeng_page,
    Product,
    logo,
    c_product,
    Cart,
    WishlistItem,
    addres
)

def base(request):
    cart = Cart.objects.all()
    lp = {
        "cart" : cart
    }
    return render(request, "base.html", lp)




# Create your views here.
def index(request):
    page = Ladeng_page.objects.all()
    n = len(page)
    li = logo.objects.all()
    cp = c_product.objects.all()
    products = Product.objects.all()
    cart = Cart.objects.all()
    lp = {
        "page": page,
        "rang": range(n),
        "logo": li,
        "c_p": cp,  
        "products": products,
        "cart" : cart
    }
    return render(request, "index.html", lp)

def man_product(request):
    page = Ladeng_page.objects.all()
    n = len(page)
    li = logo.objects.all()
    cp = c_product.objects.all()
    products = Product.objects.all()
    cart = Cart.objects.all()
    lp = {
        "page": page,
        "rang": range(n),
        "logo": li,
        "c_p": cp,  
        "products": products,
        "cart" : cart
    }
    return render(request, "man-product.html",lp)

def woman_product(request):
    page = Ladeng_page.objects.all()
    n = len(page)
    li = logo.objects.all()
    cp = c_product.objects.all()
    products = Product.objects.all()
    cart = Cart.objects.all()
    lp = {
        "page": page,
        "rang": range(n),
        "logo": li,
        "c_p": cp,  
        "products": products,
        "cart" : cart
    }
    return render(request, "woman-product.html",lp)

def kids_product(request):
    page = Ladeng_page.objects.all()
    n = len(page)
    li = logo.objects.all()
    cp = c_product.objects.all()
    products = Product.objects.all()
    cart = Cart.objects.all()
    lp = {
        "page": page,
        "rang": range(n),
        "logo": li,
        "c_p": cp,  
        "products": products,
        "cart" : cart
    }
    return render(request, "kids-product.html",lp)


def signup(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['cpassword']

        if len(uname) > 10 :
            messages.error(request, 'Username must be less than 10 characters.')
            return redirect('signup')

        if not uname.isalnum() :
            messages.error(request, 'Username must be Alphanumeric.')
            return redirect('signup')

        if pass1 != pass2 :
            messages.error(request, 'Password does not match.')
            return redirect('signup')
        

        myuser=User.objects.create_user(uname, email, pass1 )
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been successfully created.") 
        return redirect('home') 
    return render(request, "signup.html")

def hlogin(request):
    if request.method == 'POST':
        luname = request.POST['luname']
        lpass = request.POST['lpassword']

        user = authenticate(username=luname, password=lpass)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In.")
            return redirect('home')
        else:
            messages.error(request, "Invalid Username or Password.")
            return redirect('login')

    return render(request, "login.html")

def my_logout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out.")
    return redirect('home')
    

def contact(request):
    return render(request, "index.html")

def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(pk=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart.quantity = 1
            cart.save()
        return redirect('cart')
    else:
        return redirect('signup')

def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    cart_quntity = len(cart_items)
    cart = Cart.objects.all()  
    li = logo.objects.all() 

    i_total = 0
    for item in cart_items:
        i_total += item.product.p_price * item.quantity

    total = i_total + 99
    ci = {
        'cart_items': cart_items,
         "logo": li,
        'total': len(cart_items),
        'cart' : cart,
        'total_price' : total,
        'item_total' : i_total
    } 
    return render(request, 'cart.html', ci)


def remove_from_cart(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(pk=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user, product=product)
        cart.delete()
        return redirect('cart')
    else:
        return redirect('signup')

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    product_d = Product.objects.all()
    li = logo.objects.all()
    cart = Cart.objects.all()
    pd = {
        'product_id' : product,
        "logo": li,
        'product_d' : product_d,
        'cart' : cart
    }
    return render(request, 'product-detail.html', pd)

def checkout(request):
    return render(request, 'payment/checkout.html')


def add_to_wishlist(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        wishlist_item = WishlistItem(user=request.user, product=product)
        wishlist_item.save()
    else:
        return redirect('login')
    return redirect('wishlist')

def wishlist(request):
    wishlist = WishlistItem.objects.all()   
    item = WishlistItem.objects.filter(user=request.user)
    cp = c_product.objects.all()
    products = Product.objects.all()
    li = logo.objects.all()
    cart = Cart.objects.all()
    ci = {
        'wishlist': wishlist,
        'item' : item,
        "logo": li,
        'cart' : cart,
        "c_p": cp,  
        "products": products,

    } 
    return render(request, 'wishlist.html', ci)

def remove_from_wishlist(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(pk=product_id)
        wishlist_item = WishlistItem.objects.get(user=request.user, product=product)
        wishlist_item.delete()
        return redirect('wishlist')
    else:
        return redirect('login')

def address(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        address = request.POST['address']
        post_code = request.POST['post_code']
        city = request.POST['city']
        state = request.POST['state']
        addres.user_n = User.objects.get(username=request.user)
        addres.phone = phone
        addres.address = address
        addres.city = city
        addres.state = state
        addres.post_code = post_code 
        addres.save()
        return redirect('checkout')
    return render(request, 'payment/address.html')
    

    
