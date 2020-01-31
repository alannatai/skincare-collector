from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Skincare, Ingredient, Photo
from .forms import ProgressForm

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'skincare-collector'

class SkincareCreate(LoginRequiredMixin, CreateView):
  model = Skincare
  fields = '__all__'
  success_url = '/skincare/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class SkincareUpdate(LoginRequiredMixin, UpdateView):
  model = Skincare
  fields = ['price', 'star_ingredients', 'rating', 'buy_again', 'pros', 'cons']

class SkincareDelete(LoginRequiredMixin, DeleteView):
  model = Skincare
  success_url = '/skincare/'

def home(request):
  return redirect('index')

def about(request):
  return render(request, 'about.html')

@login_required
def skincare_index(request):
  skincare = Skincare.objects.filter(user=request.user)
  return render(request, 'skincare/index.html', { 'skincare': skincare }) 

@login_required
def skincare_detail(request, skincare_id):
  skincare = Skincare.objects.get(id=skincare_id)
  ingredients_skincare_doesnt_have = Ingredient.objects.exclude(id__in = skincare.ingredients.all().values_list('id'))
  progress_form = ProgressForm()
  return render(request, 'skincare/detail.html', { 
    'skincare': skincare,
    'progress_form': progress_form,
    'ingredients': ingredients_skincare_doesnt_have
  })

@login_required
def add_progress(request, skincare_id):
  form = ProgressForm(request.POST)
  if form.is_valid():
    new_progress = form.save(commit=False)
    new_progress.skincare_id = skincare_id
    new_progress.save()
  return redirect('detail', skincare_id=skincare_id)

@login_required
def assoc_ingredient(request, skincare_id, ingredient_id):
  Skincare.objects.get(id=skincare_id).ingredients.add(ingredient_id)
  return redirect('detail', skincare_id=skincare_id)

@login_required
def unassoc_ingredient(request, skincare_id, ingredient_id):
  Skincare.objects.get(id=skincare_id).ingredients.remove(ingredient_id)
  return redirect('detail', skincare_id=skincare_id)

@login_required
def add_photo(request, skincare_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, skincare_id=skincare_id)
      photo.save()
    except:
        print('An error occurred uploading file to S3')
  return redirect('detail', skincare_id=skincare_id)

class IngredientList(LoginRequiredMixin, ListView):
  model = Ingredient

class IngredientDetail(LoginRequiredMixin, DetailView):
  model = Ingredient

class IngredientCreate(LoginRequiredMixin, CreateView):
  model = Ingredient
  fields = '__all__'

class IngredientUpdate(LoginRequiredMixin, UpdateView):
  model = Ingredient
  fields = ['name', 'details']

class IngredientDelete(LoginRequiredMixin, DeleteView):
  model = Ingredient
  success_url = '/ingredients/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)