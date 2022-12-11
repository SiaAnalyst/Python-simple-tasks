import pickle


def write_contacts_to_file(filename, contacts):
    with open(filename, "wb") as fh:
        pickle.dump(contacts, fh)


def read_contacts_from_file(filename):
    with open(filename, "rb") as fh:
        unpacked = pickle.load(fh)
    return unpacked


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