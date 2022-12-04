def is_valid_password(password):
    if len(password) < 8:
        return False
    else:
        constrain_1 = any(symb.isupper() for symb in password)
        constrain_2 = any(symb.islower() for symb in password)
        constrain_3 = any(symb.isdigit() for symb in password)
        if constrain_1:
            if constrain_2:
                if constrain_3:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
