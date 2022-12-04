def format_ingredients(items):
    if len(items) > 1:
        items_str = ', '.join(items[:-1])
        items_str += ' and ' + items[-1]
    else:
        items_str = ''.join(items)
    return items_str


print(format_ingredients(["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]))