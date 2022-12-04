def is_valid_pin_codes(pin_codes):
    if pin_codes == []:
        return False
    elif sorted(pin_codes) != list(set(pin_codes)):
        return False
    else:
        for i in pin_codes:
            if len(i) != 4:
                return False
            else:
                if isinstance(i, str):
                    for j in i:
                        try:
                            a = isinstance(int(j), int)
                        except:
                            return False
                else:
                    return False
        return True


print(is_valid_pin_codes(['1101', '9034', '0011']))