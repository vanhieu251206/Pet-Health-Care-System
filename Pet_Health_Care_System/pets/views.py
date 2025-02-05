from django.shortcuts import render
from rest_framework import viewsets
from .models import Pet
from .serializers import PetSerializer

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

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


