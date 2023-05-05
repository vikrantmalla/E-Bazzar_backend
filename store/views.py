from django.shortcuts import render
from .models import Product

# Create your views here.
def store(request):
	items = Product.objects.all()
	context = {
		'items' : items
	}
	return render(request, 'store/store.html', context)