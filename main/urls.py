from django.urls import path
from . import views





app_name = 'main'
urlpatterns = [
    path('',views.Top,name="Top"),
    path('foodindex/',views.foodindex,name="foodindex"),
    path('foodwisdom',views.foodwisdom,name="foodwisdom"),
    path('recipe/',views.recipe,name="recipe"),
    path('food_rank',views.food_rank,name="food_rank"),
    path('index_top',views.index_top,name="index_top"),
    path('create_index',views.create_index,name="create_index"),
    path('create_index2',views.create_index2,name="create_index2"),
    path('edit_index/<int:num>',views.edit_index,name="edit_index"),
    path('delete_index/<int:num>',views.delete_index,name="delete_index"),
    path('find_index/',views.find_index,name="find_index"),
    path('detail_recipe/<int:num>',views.detail_recipe,name="detail_recipe"),
    path('ocr/',views.ocr,name="ocr"),
    path('detailbook',views.detailbook,name="detailbook"),
]
