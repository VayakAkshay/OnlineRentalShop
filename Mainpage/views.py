from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import ProductData,CartData,ContactForm,OrderItem
import stripe

# Create your views here.

def Homepage(request):
    products = ProductData.objects.all().values()[:5]
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        password = request.POST.get("pass")
        cpass = request.POST.get("cpass")
        if password == cpass:
            myuser = User.objects.create_user(email,mobile,password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            user = authenticate(username = email,password = password)
            login(request,user)
            messages.success(request,"You are Logged in successfully")
            return redirect("/")
        else:
            messages.warning(request,"Password is not matched ")
            return redirect("/password/")
    return render(request,"Mainpage/index.html",{"products":products})

def AboutPage(request):
    return render(request, "Mainpage/about.html")

def Costumepage(request):
    products = ProductData.objects.all()
    return render(request,"Mainpage/costume.html",{"products":products})

def FestivalPage(request):
    products = ProductData.objects.filter(product_cat = "Festival").all()
    return render(request,"Mainpage/costume.html",{"products":products})

def HalloweenPage(request):
    products = ProductData.objects.filter(product_cat = "Halloween").all()
    return render(request,"Mainpage/costume.html",{"products":products})

def MarriagePage(request):
    products = ProductData.objects.filter(product_cat = "Marriage").all()
    return render(request,"Mainpage/costume.html",{"products":products})

def PatrioticPage(request):
    products = ProductData.objects.filter(product_cat = "Patriotic").all()
    return render(request,"Mainpage/costume.html",{"products":products})

def PartyPage(request):
    products = ProductData.objects.filter(product_cat = "Party").all()
    return render(request,"Mainpage/costume.html",{"products":products})

def MyProduct(request,id):
    products = ProductData.objects.filter(id = id).all()
    return render(request,"Mainpage/product.html",{"products":products})

def Mycart(request):
    try:
        user = request.user
        cartdata = CartData()
        if request.method == "POST":
            ids = request.POST.get("product_id")
            qty = int(request.POST.get("qtys"))
            cartdata.product_id = ids
            cartdata.qty = qty
            cartdata.user_id = user.id
            cartdata.save()
        mycartlist = []
        total_price = 0
        mycartdata = CartData.objects.filter(user_id = user.id).all().values()  
        for i in mycartdata:
            mycartdic = {}
            product_data = ProductData.objects.filter(id = i["product_id"]).values()[0]
            mycartdic["cart_id"] = i["id"]
            mycartdic["product_img"] = product_data["product_img"]
            mycartdic["product_name"] = product_data["product_name"]
            price = product_data["product_price"]
            mycartdic["product_qty"] = i["qty"]
            mycartdic["product_price"] = price * i["qty"]
            total_price = total_price + (price * i["qty"])
            mycartlist.append(mycartdic)
        return render(request,"Mainpage/cart.html",{"mycartdata":mycartdata,"mycartlist":mycartlist,"total_price":total_price})
    except:
        messages.warning(request, "Please first login after then buy the product")
        return redirect("/")
def RemoveItem(request):
    if request.method == "POST":
        cart_id = request.POST.get("cart_id")
        CartData.objects.filter(id = cart_id).delete()
    return redirect("/Mycart/")

def MyProfile(request):
    user = request.user
    order_data = OrderItem.objects.filter(user_id = user.id).all().values()
    order_datas = []
    for i in order_data:
        mydic = {}
        product_data = ProductData.objects.filter(id = i["product_id"]).all().values()[0]
        mydic["product_img"] = product_data["product_img"]
        mydic["product_name"] = product_data["product_name"]
        mydic["qty"] = i["qty"]
        mydic["product_price"] = product_data["product_price"]
        order_datas.append(mydic)
    return render(request,"Mainpage/profile.html",{"order_datas":order_datas})

def EditProfile(request):
    user = request.user
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        phone = request.POST.get("mobile")
        User.objects.filter(id = user.id).update(first_name = fname)
        User.objects.filter(id = user.id).update(last_name = fname)
        User.objects.filter(id = user.id).update(username = email)
        User.objects.filter(id = user.id).update(email = phone)
        return redirect('/profile/')
    return render(request, "Mainpage/edit_profile.html")

def contactPage(request):
    contact = ContactForm()
    if request.method == "POST":
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact.email = email
        contact.message = message
        contact.save()
        messages.success(request,"Your form submitted successfully")
        return redirect("/contact/")
    return render(request,"Mainpage/contact.html")

def OrderPage(request):
    return render(request,"Mainpage/order.html")

stripe.api_key = 'sk_test_51MedHmSHJDFuPL5cnRItHVU94xOAzKltL5vuoADjGI0wZfVNRtCwU3I3eKgvtQUF0z3w2yl5IuQ5rRZcOs9m2ytj00YSZRJhjw'
def checkout(request):
    user = request.user
    if request.method == "POST":
        total_price = 0
        cart_data = CartData.objects.filter(user_id=user.id).all().values()
        line_items = []
        total_price = 0
        for i in range(0,len(cart_data)):
            product_id = cart_data[i]["product_id"]
            product_data = ProductData.objects.filter(id = product_id).all().values()[0]
            total_price = total_price + product_data["product_price"]
            line_items.append(
            {
                'price_data': {
                    'currency': 'inr',
                    'product_data': {
                    'name': product_data["product_name"],
                    },
                    'unit_amount': int(product_data["product_price"] * 100),
                },
                'quantity': cart_data[i]["qty"],
            })
        print(line_items)
        session = stripe.checkout.Session.create(
        line_items= line_items,
        mode='payment',
        success_url='http://127.0.0.1:8000/success/',
        cancel_url='http://127.0.0.1:8000/cancle/',
        )
        return redirect(session.url, code=303)
    return redirect('/')

def success_page(request):
    user = request.user
    cart_item = CartData.objects.filter(user_id = user.id).all().values()
    for i in cart_item:
        print(i)
        order_item = OrderItem()
        order_item.product_id = i["product_id"]
        order_item.qty = i["qty"]
        order_item.user_id = user.id
        order_item.save()
    CartData.objects.filter(user_id = user.id).delete()
    return render(request,"Mainpage/success.html")

def cancle_page(request):
    return render(request,"Mainpage/cancle.html")

def logout_page(request):
    logout(request)
    return redirect("/")
# 4500 3800 1500 