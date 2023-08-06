print('-' * 50)

def display_det(*scr, **det):
    print(scr, '-', type(scr))
    print(det, '-', type(det))

print(display_det, '-', type(display_det))

print('-' * 50)

def sqr(n):
    return n ** 2

print('SQR of 5 -', sqr(5))

print('-' * 50)

# Lambda Expressions
sqr = lambda n: n ** 2
print(sqr, '-', type(sqr))
print('SQR of 25 -', sqr(25))

print('-' * 50)

# Sum of the numbers passed as the parameter
calc_sum = lambda *nums: sum(nums)
print('Sum 1 -', calc_sum(1, 2, 3, 4, 5))
print('Sum 2 -', calc_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

print('-' * 50)

# Map
sqr = lambda n: n ** 2
sqr_list = list(map(sqr, [1, 2, 3, 4, 5]))

# [sqr(1), sqr(2), sqr(3), sqr(4), sqr(5)]
print('SQR List -', sqr_list)
for elem in sqr_list:
    print('Element -', elem)

print('-' * 50)

# Filter
chk_palin = lambda string: string == string[::-1]
string_list = ['php', 'perl', '1221', 'python', 'madam']
palin_list = list(filter(chk_palin, string_list))
print('Palin List -', palin_list)

print('-' * 50)

# Reduce
from functools import reduce
factorial = lambda n1, n2, n3=2: n1 * n2 * n3
'''
range(1, 6) => [1, 2, 3, 4, 5]
factorial(1, 2) => 2
factorial(2, 3) => 6
factorial(6, 4) => 24
factorial(24, 5) => 120
'''
fact = reduce(factorial, range(1, 6))
print('Fact -', fact)

var = 1
var = True
var = [1, 2]

print('-' * 50)

# Class
class Employee:
    company = 'THBS'
    
    # Initialization method
    def __init__(self, name, loc, sal=5000):
        self.name = name
        self.loc = loc
        self.__sal = sal
        self.company = 'THIS'
        print('Object Initialized -', self)

    def display_emp(self):
        return f'{self.name} from {self.loc} earns Rs.{self.__sal}'

    def get_sal(self):
        return self.__sal

obj = Employee('justin', 'bangalore', 25000)
print('Method -', obj.display_emp())

print('Name -', obj.name)
print('Sal -', obj.get_sal())
print('Company Using Class -', Employee.company)
print('Company Using Object -', obj.company)

obj_1 = Employee(loc='Pune', name='Tris')
print('Method -', obj_1.display_emp())

print('-' * 50)

# Inheritance
class A:
    num = 5
    
    def __init__(self):
        self.num = 25
        print('In A')

class B(A):
    pass

class C(A):
    def __init__(self):
        # Call to super init explicitly
        A.__init__(self)         # super().__init__()
        
        self.power = 2
        print('In C')

    def calc(self):
        return self.num ** self.power

obj_B = B()
obj_C = C()
print('num using object c -', obj_C.num)
print('power using object c -', obj_C.power)
print('calc -', obj_C.calc())

print('-' * 50)

class D(B):
    pass

obj_D = D()

class E:
    def __init__(self):
        print('In E')

class F(E, A):
    def __init__(self):
        super().__init__()

obj_F = F()

print('-' * 50)

# Exception Handling
try:
    print(1/1)
    print(2 + 3)
except (ZeroDivisionError, AttributeError) as e:
    print(f'CE Occurred: {e}')
except TypeError as e:
    print(f'TE Occurred: {e}')
except Exception as e:
    print(f'Error Occurred: {e.__class__.__name__} => {e}')
else:
    print('ELSE - No Exceptions')
finally:
    print('FINALLY - Always be Executed')
    
print('After Statements')

print('-' * 50)

def f1():
    try:
        print('S1')
        return 1
    finally:
        return 2

print('Returns -', f1())

print('-' * 50)

