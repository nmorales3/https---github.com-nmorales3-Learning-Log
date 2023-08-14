import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","pizzeria.settings")


import django
django.setup()

from Pizzas.models import *

pizzas= Pizza.objects.all()
print(pizzas)

for pizza in pizzas:
    print(pizza.id, pizza, pizza.date_added)

p= Pizza.objects.get(id=1)
print(p.pizza_name)
print(p.date_added)

toppings=Topping.objects.filter(pizza=p)

for t in toppings:
    print(t.id, t)