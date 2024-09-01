from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FoodRecipe
from .serializers import FoodItemSerializer  # Updated import

@api_view(['GET'])
def list_food_items(request):
    category = request.query_params.get('category')
    queryset = FoodRecipe.objects.all() if not category else FoodRecipe.objects.filter(category=category)
    
    serializer = FoodItemSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_food_item(request):
    serializer = FoodItemSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PATCH'])
def update_food_item(request, id=None):
    try:
        food_item = FoodRecipe.objects.get(id=id)
    except FoodRecipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = FoodItemSerializer(food_item, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
