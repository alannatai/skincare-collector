from django.shortcuts import render
from django.http import HttpResponse

from .models import Skincare

def home(request):
  return HttpResponse('<h1>Home</h1>')

def about(request):
  return render(request, 'about.html')

def skincare_index(request):
  skincare = Skincare.objects.all()
  return render(request, 'skincare/index.html', { 'skincare': skincare }) 

def skincare_detail(request, skincare_id):
  product = Skincare.objects.get(id=skincare_id)
  return render(request, 'skincare/detail.html', { 'product': product })