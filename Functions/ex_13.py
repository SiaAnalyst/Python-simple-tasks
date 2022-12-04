def cost_delivery(quantity, *args, discount = 0):
    if quantity > 0:
        cost = 1*5 + (quantity - 1) * 2
        cost_discount = cost - cost * discount
    else:
        cost_discount = 0
    return cost_discount


print(cost_delivery(2, 1, 2, 3) == 7)
print(cost_delivery(3, 3) == 9)
print(cost_delivery(1) == 5)
print(cost_delivery(2, 1, 2, 3, discount=0.5) == 3.5)