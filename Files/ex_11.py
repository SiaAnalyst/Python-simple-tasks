def get_credentials_users(path):
    list = []
    with open(path, 'rb') as file:
        for i in file.readlines():
            list.append(i.decode().removesuffix('\n'))
    return list