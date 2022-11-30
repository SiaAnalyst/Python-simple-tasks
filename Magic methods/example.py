class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def say_hello(self):
        return f'Hello! I am {self.name}'


bill = Human('Bill')
print(bill.say_hello())  # Hello! I am Bill
print(bill.age)  # 0

jill = Human('Jill', 20)
print(jill.say_hello())  # Hello! I am Jill
print(jill.age)  # 20

print('--------------------')


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point ({self.x}, {self.y})'


a = Point(1, 9)
print(a)

print('--------------------')


class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Hello! I am {self.name}'


bill = Human('Bill')
bill_str = str(bill)
print(bill_str)  # Hello! I am Bill

print('--------------------')


class ListedValuesDict:
    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        if key in self.data:
            self.data[key].append(value)
        else:
            self.data[key] = [value]

    def __getitem__(self, key):
        result = str(self.data[key][0])
        for value in self.data[key][1:]:
            result += ", " + str(value)
        return result


l_dict = ListedValuesDict()
l_dict[1] = 'a'
l_dict[1] = 'b'
print(l_dict[1])  # a, b

print('--------------------')


class Adder:
    def __init__(self, add_value):
        self.add_value = add_value

    def __call__(self, value):
        return self.add_value + value


two_adder = Adder(2)
print(two_adder(5))  # 7
print(two_adder(4))  # 6

three_adder = Adder(3)
print(three_adder(5))  # 8
print(three_adder(4))  # 7

print('--------------------')


class Session:
    def __init__(self, addr, port=8080):
        self.connected = True
        self.addr = addr
        self.port = port

    def __enter__(self):
        print(f"connected to {self.addr}:{self.port}")
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.connected = False
        if exception_type is not None:
            print("Some error!")
        else:
            print("No problem")


print('--------------------')

localhost_session = Session("localhost")

with localhost_session as session:
    print(session is localhost_session)  # True
    print(localhost_session.connected)  # True

print(localhost_session.connected)  # False

print('--------------------')

with Session("localhost") as session:
    print(session.connected)  # True

print('--------------------')

# error
# with Session("host", "port") as session:
#     raise Exception("OH NO!")

print('--------------------')


# iterator
class Iterable:
    MAX_VALUE = 10

    def __init__(self):
        self.current_value = 0

    def __next__(self):
        if self.current_value < self.MAX_VALUE:
            self.current_value += 1
            return self.current_value
        raise StopIteration


class CustomIterator:
    def __iter__(self):
        return Iterable()


c = CustomIterator()
for i in c:
    print(i)


# encapsulation
class Secret:
    public_field = 'this is public'
    _private_field = 'avoid using this please'
    __real_secret = 'I am hidden'


s = Secret()
print(s.public_field)  # this is public
print(s._private_field)  # avoid using this please
print(s._Secret__real_secret)  # I am hidden


class PositiveNumber:
    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value > 0:
            self.__value = new_value
        else:
            print('Only numbers greater zero accepted')


p = PositiveNumber()
p.value = 1
print(p.value)  # 1
p.value = -1    # Only numbers greater zero accepted
p._PositiveNumber__value = -1
print(p.value)  # -1s


from collections import UserDict


class MyDict(UserDict):
    def __add__(self, other):
        self.data.update(other)
        return self

    def __sub__(self, other):
        for key in other:
            if key in other:
                self.data.pop(key)
        return self


d1 = MyDict({1: 'a', 2: 'b'})
d2 = MyDict({3: 'c', 4: 'd'})

d3 = d1 + d2
print(d3)   # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

d4 = d3 - d2
print(d4)   # {1: 'a', 2: 'b'}


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y


Point(0, 0) == Point(0, 0)  # True
Point(0, 0) != Point(0, 0)  # False
Point(0, 0) < Point(1, 0)   # False
Point(0, 0) > Point(0, 1)   # False
Point(0, 2) >= Point(0, 1)  # True
Point(0, 0) <= Point(0, 0)  # True