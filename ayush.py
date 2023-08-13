from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FoodDonation

class DonateFoodAPI(APIView):
    def post(self, request):
        data = request.data

        food_item = data.get("food_item")
        fruits = data.get("fruits", False)
        vegetables = data.get("vegetables", False)
        south_indian_cuisine = data.get("south_indian_cuisine", False)
        north_indian_cuisine = data.get("north_indian_cuisine", False)

        FoodDonation.objects.create(
            food_item=food_item,
            fruits=fruits,
            vegetables=vegetables,
            south_indian_cuisine=south_indian_cuisine,
            north_indian_cuisine=north_indian_cuisine
        )

        return Response({"message": "Food donation details added successfully"})






from djongo import models

class FoodDonation(models.Model):
    food_item = models.CharField(max_length=100)
    fruits = models.BooleanField(default=False)
    vegetables = models.BooleanField(default=False)
    south_indian_cuisine = models.BooleanField(default=False)
    north_indian_cuisine = models.BooleanField(default=False)
