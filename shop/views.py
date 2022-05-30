from django.shortcuts import render
from .models import Category, Product
from .serializers import CategorySerializer
from rest_framework.views import APIView

def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)

class CategoryViewSet(APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
