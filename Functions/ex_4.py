base_rate = 40
price_per_km = 10
total_trip = 0


def trip_price(path):
    global total_trip
    total_trip += 1
    price = base_rate + price_per_km * path
    return price


print(trip_price(4.3))
