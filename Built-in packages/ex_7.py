import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    list = []
    for i in cats:
        if not isinstance(i, dict):
            list.append({'nickname': i.nickname, 'age': i.age, 'owner': i.owner})
        if isinstance(i, dict):
            list.append(Cat(i['nickname'], i['age'], i['owner']))
    return list