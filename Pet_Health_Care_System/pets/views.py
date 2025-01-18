from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'pets/index.html', context)

def login(request):
    context = {}
    return render(request, 'pets/login.html', context)

def quenmk(request):
    context = {}
    return render(request, 'pets/quenmk.html', context)


