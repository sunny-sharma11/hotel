from django.shortcuts import render
from django.http import HttpResponse
from .models import Hotels

# Create your views here.

def index(request):

    hotl = Hotels.objects.all()
    return render(request, 'index.html', {'hotl':hotl})
