from django.shortcuts import render
from shop.models import Shop
# Create your views here.

def index(request):
	return render (request, 'index.html', {})