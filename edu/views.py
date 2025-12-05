from django.shortcuts import render
from django.http import HttpResponse
from .models import OquvMarkaz, Yonalish

def home_page(request):
    yonalishlar = Yonalish.objects.all().order_by('id')
    hamma_markazlar = OquvMarkaz.objects.all().order_by('-id') 
    context = {'markazlar': hamma_markazlar,'yonalishlar': yonalishlar}
    
    return render(request, 'index.html', context)

def filter_markazlar(request, kat_id):
    yonalishlar = Yonalish.objects.all().order_by('id')
    kurslar = OquvMarkaz.objects.filter(yonalish_id=kat_id).order_by('-id')
    context = {'markazlar': kurslar, 'yonalishlar': yonalishlar}
    
    return render(request, 'index.html', context)

def batafsil_malumot(request, pk):
    markaz = OquvMarkaz.objects.filter(id=pk).first() 
    
    return render(request, 'detail.html', {'markaz': markaz})
