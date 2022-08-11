from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.serializers import OrderSerializer
from .models import Order
# Create your views here.


class OrdersData(APIView):
    def get(self, request, format=None):
        order=Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)