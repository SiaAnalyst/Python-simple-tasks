import shutil


def create_backup(path, file_name, employee_residence):
    with open(path + '/' + file_name, 'wb') as file:
        for k, v in employee_residence.items():
            file.write(f'{k} {v}\n'.encode())
    return shutil.make_archive('backup_folder', 'zip', path)