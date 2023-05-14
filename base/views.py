from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
@api_view(['GET'])
def index(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many = True)
    return Response(serializer.data)