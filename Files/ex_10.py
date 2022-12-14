def save_credentials_users(path, users_info):
    with open(path, 'wb') as fh:
        for k, v in users_info.items():
            fh.write(f'{k}:{v}\n'.encode())