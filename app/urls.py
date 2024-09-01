from django.urls import path
from .views import list_food_items, create_food_item, update_food_item

urlpatterns = [
    path('fooditems/', list_food_items, name='list-food-items'),          # GET: List food items
    path('fooditems/create/', create_food_item, name='create-food-item'), # POST: Create a food item
    path('fooditems/<int:id>/update/', update_food_item, name='update-food-item'),  # PATCH: Update a food item
]
