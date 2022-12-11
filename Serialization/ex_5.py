import json


def write_contacts_to_file(filename, contacts):
    data = {'contacts':[i for i in contacts]}
    with open(filename, "w") as fh:
        json.dump(data, fh)


def read_contacts_from_file(filename):
    with open(filename, "r") as fh:
        unpacked = json.load(fh)
    return unpacked['contacts']


if __name__ == '__main__':
    filename = 'data.bin'
    contact = {
        "name": "Marry Hanson",
        "email": "example@gmail.com",
        "phone": "(999) 111-1111",
        "favorite": False,
    }

    write_contacts_to_file(filename, contact)
    read_contacts_from_file(filename)