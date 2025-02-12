from django.shortcuts import render

# Tạo view cho Dashboard
def dashboard(request):
    return render(request, 'QTV/dashboard.html')

def QL(request):
    return render(request, 'QTV/QL.html')

def CH(request):
    return render(request, 'QTV/CH.html')

def BC(request):
    return render(request, 'QTV/BC.html')



