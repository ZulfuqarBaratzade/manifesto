from django.shortcuts import render
from core.models import *
# Create your views here.

def layout(request):
    logo = Logo.objects.get(name='logo_image').file
    mainlogo = MainBanner.objects.all()
    food = Food.objects.all()
    dessert = Dessert.objects.all()
    lunch = BussinessLunch.objects.all()
    drink = Drink.objects.all()
    text = TextGoal.objects.all()
    link = SocialMedia.objects.all()
    context = {
        'logo':logo,
        'mainlogo':mainlogo,
        'food':food,
        'dessert':dessert,
        'lunch':lunch,
        'drink':drink,
        'text':text,
        'link':link,
    }
    return context
def index(request):
    return render(request,'index.html')