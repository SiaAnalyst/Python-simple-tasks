def get_recipe(path, search_id):
    lines = []
    with open(path, 'r') as f:
        for i in f.readlines():
            lines.append(i.strip('\n').split(','))
    recipe_info = []
    for i in lines:
        dict = {}
        dict['id'] = i[0]
        dict['name'] = i[1]
        dict['ingredients'] = [i[2],i[3],i[4]]
        recipe_info.append(dict)
    recipe = {}
    for i in recipe_info:
        if i['id'] == search_id:
            recipe = i
            return recipe
        else:
            return None