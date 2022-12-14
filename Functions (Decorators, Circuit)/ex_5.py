def format_phone_number(func):
    def inner(phone):
        result = func(phone)
        if len(result)<11:
            result = '+38'+result
        else:
            result = '+'+result
        return result
    return inner


@format_phone_number
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