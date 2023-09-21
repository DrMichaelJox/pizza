from django.shortcuts import render
from api.models import Pizza

def templateHello(request):
    return render(request, "hello.html")

def templatePizza(request):
    pizzas = []
    for pizza in Pizza.objects.all():
        pizzas.append({"name":pizza.name, "price":pizza.price})
    return render(request, "pizza.html",{"pizzas":pizzas})


