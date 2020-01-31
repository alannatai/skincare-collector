from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('skincare/', views.skincare_index, name='index'),
  path('skincare/<int:skincare_id>/', views.skincare_detail, name='detail'),
  path('skincare/create/', views.SkincareCreate.as_view(), name='skincare_create'),
  path('skincare/<int:pk>/update/', views.SkincareUpdate.as_view(), name='skincare_update'),
  path('skincare/<int:pk>/delete/', views.SkincareDelete.as_view(), name='skincare_delete'),
  path('skincare/<int:skincare_id>/add_progress/', views.add_progress, name='add_progress'),
  path('skincare/<int:skincare_id>/add_photo/', views.add_photo, name='add_photo'),

  path('skincare/<int:skincare_id>/assoc_ingredient/<int:ingredient_id>/', views.assoc_ingredient, name='assoc_ingredient'),
  path('skincare/<int:skincare_id>/unassoc_ingredient/<int:ingredient_id>/', views.unassoc_ingredient, name='unassoc_ingredient'),
  path('ingredients/', views.IngredientList.as_view(), name='ingredients_index'),
  path('ingredients/<int:pk>/', views.IngredientDetail.as_view(), name='ingredients_detail'),
  path('ingredients/create/', views.IngredientCreate.as_view(), name='ingredients_create'),
  path('ingredients/<int:pk>/update/', views.IngredientUpdate.as_view(), name='ingredients_update'),
  path('ingredients/<int:pk>/delete/', views.IngredientDelete.as_view(), name='ingredients_delete'),

  path('accounts/signup', views.signup, name='signup'),
]