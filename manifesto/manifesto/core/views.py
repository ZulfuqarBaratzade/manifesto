from django.shortcuts import render
from core.models import *
# Create your views here.

def layout(request):
    logo = Logo.objects.get(name='logo_image').file
    mainlogo = MainBanner.objects.all()
    context = {
        'logo':logo,
        'mainlogo':mainlogo,
    }
    return context
def index(request):
    return render(request,'index.html')