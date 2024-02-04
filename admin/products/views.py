from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .producer import publish
from .models import Product, User
from .serializers import ProductSerializer
import random


class ProductViewSet(viewsets.ViewSet):
    def list(self, request): #List of the products
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def create(self, request): #/api/products
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('Product Created',serializer.data)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    def retrieve(self, request,pk=None): #/api/products/<string>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def update(self, request,pk=None): #/api/products/<string>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('Product Updated',serializer.data)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        
        
    def destroy(self, request,pk=None): #/api/products/<string>
        product = Product.objects.get(id=pk)
        product.delete()
        publish('Product Deleted',pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserApiView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })
        
    