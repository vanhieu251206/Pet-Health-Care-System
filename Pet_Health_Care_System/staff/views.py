from django.shortcuts import render, redirect

def staff_dashboard(request):
    context = {}
    return render(request, 'staff/staff_dashboard.html', context)