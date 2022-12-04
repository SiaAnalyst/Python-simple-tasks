def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price - price * discount
        return price

    apply_discount()
    return price


print(discount_price(10, 0.1))
