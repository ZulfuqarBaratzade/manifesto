from django.shortcuts import render
from core.models import *
# Create your views here.

def layout(request):
    logo = Logo.objects.get(name='logo_image').file
    context = {
        'logo':logo,
    }
    return context
def index(request):
    return render(request,'index.html')