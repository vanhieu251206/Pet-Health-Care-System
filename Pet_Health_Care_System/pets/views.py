from django.shortcuts import render

# Create your views here.
def guest_dashboard(request):
    context = {}
    return render(request, 'pets/guest_dashboard .html', context)

def login(request):
    context = {}
    return render(request, 'pets/login.html', context)

def quenmk(request):
    context = {}
    return render(request, 'pets/quenmk.html', context)


