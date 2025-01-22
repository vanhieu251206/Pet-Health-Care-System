from django.shortcuts import render

# Trang chủ
def index(request):
    context = {}  # Dữ liệu truyền vào template (hiện tại để trống)
    return render(request, 'pets/index.html', context)

# Trang đăng nhập
def login(request):  
    context = {}
    return render(request, 'pets/login.html', context)

# Trang quên mật khẩu
def quenmk(request):  
    context = {}
    return render(request, 'pets/quenmk.html', context)

# Trang giới thiệu
def gioithieu(request):  
    context = {}
    return render(request, 'pets/gioithieu.html', context)

# Trang dangkidangki
def dangki(request):
    context = {}
    return render(request, 'pets/dangki.html', context)

# Trang lien he
def lienhe(request):
    context = {}
    return render(request, 'pets/lienhe.html', context)

# Trang dich vu
def dichvu(request):
    context = {}
    return render(request, 'pets/dichvu.html', context)

# Trang mua sam
def muasam(request):
    context = {}
    return render(request, 'pets/muasam.html', context)

# Trang kham benh 
def dichvukhambenh(request):
    context = {}
    return render(request, 'pets/dichvukhambenh.html', context)

# Trang spa
def spa(request):
    context = {}
    return render(request, 'pets/spa.html', context)

