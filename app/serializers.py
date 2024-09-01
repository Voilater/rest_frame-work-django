from rest_framework import serializers
from .models import FoodRecipe

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodRecipe
        fields = ['id', 'name', 'description', 'ingredients', 'method', 'category']

    def validate_name(self, value):
        if FoodRecipe.objects.filter(name=value).exists():
            raise serializers.ValidationError("A food item with this name already exists.")
        return value
