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

# Trang dat lich
def datlich(request):
    context = {}
    return render(request, 'pets/datlich.html', context)

<<<<<<< HEAD
@login_required
def customer_dashboard(request):
    return render(request, 'pets/customer_dashboard.html')

@login_required
def staff_dashboard(request):
    return render(request, 'pets/staff_dashboard.html')

def select_role_view(request):
    role = request.GET.get('role', None)
    if role == 'customer':
        return redirect('customer_dashboard') 
    elif role == 'staff':
        return redirect('staff_dashboard')    
    elif role == 'vet':
        return redirect('vet_dashboard')      
    elif role == 'admin':
        return redirect('admin_dashboard')    
    else:
        return HttpResponseBadRequest("Vai trò không hợp lệ.")

class PetList(APIView):
    queryset = Pet.objects.all()

    def get(self, request):  
        pets = Pet.objects.all()  
        serializer = PetSerializer(pets, many=True)  
        return Response(serializer.data) 
    
    def post(self, request):  # Thêm thú cưng mới
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Lưu thú cưng mới vào cơ sở dữ liệu
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Trả về thông tin thú cưng mới
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Trả về lỗi nếu dữ liệu không hợp lệ
    
        @login_required
    def dog_products(request):
        pets = Pet.objects.all()  # Lấy danh sách thú cưng từ cơ sở dữ liệu
        context = {'pets': pets}  # Truyền dữ liệu thú cưng vào template
        return render(request, 'pets/dog_products.html', context)
  
=======
>>>>>>> ca318054cb536b5f1be4088af93423818228af37
