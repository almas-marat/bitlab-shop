from django.shortcuts import render
from rest_framework.response import Response

from .models import Category, Product
from .serializers import ProductSerializer
from rest_framework.views import APIView


class ProductView(APIView):
    def get(self, request):
        p = Product.objects.all()
        return Response({'title': ProductSerializer(p, many=True).data})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({"error": "Objects does not exists"})

        serializer = ProductSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})




def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)

