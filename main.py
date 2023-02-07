from classes import *


weight = list(map(int, Order.GetWeight(self=Order)))
print(weight)

place = Order.GetPlace(self=Order)
print(place)

# Создание словаря с заказами

ord_dict = {}

# Список сформированных заказов

orders = []

if len(weight) == len(place):
    i = 0
    for i in range(len(weight)):
        print(weight[i])
        ord_dict[weight[i]] = place[i]

# Создание объектов класса Order(заказов)


else:
    print('Incorrect Data')
print(ord_dict)
print('Заказов сейчас: ', len(weight))

keys = list(ord_dict.keys())
values = list(ord_dict.values())
for i in range(len(weight)):
    orders.append(Order(keys[i], values[i]))
    print(orders[i].weight, orders[i].place)












