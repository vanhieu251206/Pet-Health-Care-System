from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils.http import urlencode
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib import messages
from .models import Product, Cart, CartItem
from staff.views import tong_quan
from django.urls import reverse
import logging

CustomUser = get_user_model()

logger = logging.getLogger(__name__)

# Create your views here.
def guest_dashboard(request):
    context = {}
    return render(request, 'pets/guest_dashboard.html', context)

def login_page(request):
    context = {}
    return render(request, 'pets/login_page.html', context)

def dashboard_customer(request):
    context = {}
    return render(request, 'pets/dashboard_customer.html', context)

def checkout(request):
    context = {}
    return render(request, 'pets/checkout.html', context)

def vaccination(request):
    context = {}
    return render(request, 'pets/vaccination.html', context)

def periodic_health_checkups(request):
    context = {}
    return render(request, 'pets/periodic_health_checkups.html', context)

def about_us(request):
    context ={}
    return render(request, 'pets/about_us.html', context)

def contact(request):
    context ={}
    return render(request, 'pets/contact.html', context)

def register_page(request):
    context ={}
    return render(request, 'pets/register_page.html', context)

def shop(request):
    products =  Product.objects.all()
    return render(request, 'pets/shop.html', {'products': products})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")
        next_url = request.GET.get("next", "")  

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.role == role:
                login(request, user)


                if next_url:
                    return redirect(next_url)

                if role == "customer":
                    return redirect("pets:guest_dashboard")
                elif role in ["staff", "doctor", "admin"]:
                    return redirect("staff:tong_quan")
                else:
                    messages.error(request, "Vai trò không hợp lệ.")
                    return redirect("pets:login_page")
            else:
                messages.error(request, "Vai trò không khớp với tài khoản.")
                return redirect("pets:login_page")
        else:
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng.")
            return redirect("pets:login_page")

    return render(request, "pets/login_page.html")

def register_view(request):
    if request.method == "POST":
        # Lấy dữ liệu từ form
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()
        password_confirm = request.POST.get("password_confirm", "").strip()

        # Ghi log dữ liệu nhận được
        logger.info(f"🔹 Dữ liệu nhận được - Username: {username}, Email: {email}")

        # Kiểm tra trường trống
        if not username or not email or not password or not password_confirm:
            messages.error(request, "Vui lòng điền đầy đủ thông tin.")
            return redirect("pets:register_page")

        # Kiểm tra độ dài username
        if len(username) < 3:
            messages.error(request, "Tên đăng nhập phải có ít nhất 3 ký tự.")
            return redirect("pets:register_page")

        # Kiểm tra định dạng email
        if "@" not in email or "." not in email:
            messages.error(request, "Email không hợp lệ.")
            return redirect("pets:register_page")

        # Kiểm tra mật khẩu có đủ dài không
        if len(password) < 6:
            messages.error(request, "Mật khẩu phải có ít nhất 6 ký tự.")
            return redirect("pets:register_page")

        # Kiểm tra mật khẩu xác nhận
        if password != password_confirm:
            messages.error(request, "Mật khẩu xác nhận không khớp.")
            return redirect("pets:register_page")

        # Kiểm tra username đã tồn tại chưa
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Tên đăng nhập đã tồn tại.")
            return redirect("pets:register_page")

        # Kiểm tra email đã tồn tại chưa
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email đã được sử dụng.")
            return redirect("pets:register_page")

        # Tạo tài khoản mới
        try:
            user = CustomUser.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Đăng ký thành công! Vui lòng đăng nhập.")
            logger.info(f"✅ Người dùng {username} đã được tạo thành công!")
            return redirect("pets:login_page")

        except Exception as e:
            logger.error(f"❌ Lỗi khi tạo người dùng: {str(e)}")
            messages.error(request, f"Có lỗi xảy ra: {str(e)}")
            return redirect("pets:register_page")

    return render(request, "pets/register_page.html")


def logout_view(request):
    logout(request)
    return redirect('pets:login_page')

@login_required(login_url="pets:login_page")
def cart_view(request):
    if not request.user.is_authenticated:
        next_url = request.get_full_path()  
        return redirect(f"{reverse('pets:login_page')}?{urlencode({'next': next_url})}")

    if request.user.role != "customer":
        return redirect("staff:tong_quan") 

    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.total_price() for item in cart_items)

    return render(request, "pets/cart.html", {"cart_items": cart_items, "total_price": total_price})

@login_required(login_url="pets:login_page")
def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        next_url = request.GET.get("next", "pets:cart_view")
        return redirect(f"{reverse('pets:login_page')}?next={next_url}")

    # Nếu đã đăng nhập, kiểm tra vai trò
    if request.user.role != "customer":
        #messages.warning(request, "Bạn không thể thêm sản phẩm vào giỏ hàng.")
        return redirect("staff:tong_quan")  

    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1  
        cart_item.save()

    messages.success(request, f"{product.name} đã được thêm vào giỏ hàng!")
    return redirect("pets:cart_view") 

def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect("pets:cart_view")

def update_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "increase":
            item.quantity += 1  
        elif action == "decrease" and item.quantity > 1:
            item.quantity -= 1  

        item.save()

    return redirect("pets:cart_view")


