from django.shortcuts import render

# Create your views here.
def buku(request):
    return render(request, 'buku.html')

def daftar(request):
    return render(request, 'daftar.html')

