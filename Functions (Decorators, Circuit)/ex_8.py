def get_emails(list_contacts):
    return [i for i in map(lambda i: i.get('email'), list_contacts)]