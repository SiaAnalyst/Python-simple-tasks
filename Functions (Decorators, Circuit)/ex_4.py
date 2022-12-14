def discount_price(discount):
    def get_price(price):
        price = price*(1-discount)
        return price
    return get_price