from django.shortcuts import render
from core.models import *
# Create your views here.

def layout(request):
    logo = Logo.objects.get(name='logo_image').file
    mainlogo = MainBanner.objects.all()
    food = Food.objects.all()
    dessert = Dessert.objects.all()

    context = {
        'logo':logo,
        'mainlogo':mainlogo,
        'food':food,
        'dessert':dessert,
    }
    return context
def index(request):
    return render(request,'index.html')