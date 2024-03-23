from django.shortcuts import render

# Create your views here.
def pinjam(request):
    return render(request, 'pinjam/pinjam.html')
