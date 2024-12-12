from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def guest_page(request):
    context= {}
    return render(request, 'pets/guest_page.html', context)
def login_page(request):
    context= {}
    return render(request, 'pets/login_page.html', context)
def cart(request):
    context= {}
    return render(request, 'pets/cart.html', context)
def checkout(request):
    context= {}
    return render(request, 'pets/checkout.html', context)