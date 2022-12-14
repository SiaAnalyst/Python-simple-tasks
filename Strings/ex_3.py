def sanitize_phone_number(phone):
    phone = phone.strip().replace("(", "").replace(")", "").replace("-", "").replace("+", "").replace(" ", "")
    return phone