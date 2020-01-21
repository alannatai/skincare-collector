from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('skincare/', views.skincare_index, name='index'),
  path('skincare/<int:skincare_id>/', views.skincare_detail, name='detail'),
]