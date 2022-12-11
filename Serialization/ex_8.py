import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as fh:
        field_names = [i for i in contacts[0].keys()]
        writer = csv.DictWriter(fh, fieldnames=field_names)
        writer.writeheader()
        for i in contacts:
            writer.writerow(i)


def read_contacts_from_file(filename):
    with open(filename, 'r', newline='') as fh:
        reader = csv.DictReader(fh)
    list = []
    for row in reader:
        if row['favorite'] == 'False':
            row['favorite'] = False
        if row['favorite'] == 'True':
            row['favorite'] = True
        list.append(row)
    return list


filename = 'file.dat'
contacts = [
    {'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False},
    {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False}
]


write_contacts_to_file(filename, contacts)
read_contacts_from_file(filename)