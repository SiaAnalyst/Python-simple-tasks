def get_favorites(contacts):
    return [i for i in filter(lambda i: i.get('favorite')==True, contacts)]