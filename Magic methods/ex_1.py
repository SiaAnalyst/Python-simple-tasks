# dir methods
print(dir(int))

#__add__() method
num = 10
print(num + 5)
print(num.__add__(5))

# __new__() method
class Employee:

    def __new__(cls):
        print ("__new__ magic method is called")
        inst = object.__new__(cls)
        return inst

    def __init__(self):
        print ("__init__ magic method is called")
        self.name='Satya'


emp = Employee()


#__str__() method
num = 12
print(str(num))
print(int.__str__(num))


class Employee:

    def __init__(self):
        self.name = 'Marry'
        self.salary = 10000

    def __str__(self):
        return self.name+"'s salary is $"+str(self.salary)


emp_1 = Employee()
print(emp_1)