def fun(a, b=2, c=3):
    """Finds the sum of three parameters.
    The first parameter is required, the other two are 2 and 3 by default"""
    
    return a + b * c


print(fun.__doc__)