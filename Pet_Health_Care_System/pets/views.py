from django.shortcuts import render

# Create your views here.
def guest_page(request):
    context = {}
    return render(request, 'pets/index.html', context)


