def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    dict = {
        'UA':[],
        'JP':[],
        'TW':[],
        'SG':[]
    }
    print(list_phones)

    for i in list_phones:
        i = sanitize_phone_number(i)
        if i.startswith('380'):
            dict['UA'].append(i)
        elif i.startswith('81'):
            dict['JP'].append(i)
        elif i.startswith('65'):
            dict['SG'].append(i)
        elif i.startswith('886'):
            dict['TW'].append(i)
        else:
            dict['UA'].append(i)
    #print(dict)
    return dict