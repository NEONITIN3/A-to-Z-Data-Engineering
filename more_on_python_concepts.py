print('-' * 75)

# Mutable => elements can be added, deleted or modified

lst = [1, 100]
print(lst, '-', type(lst), '-', id(lst))

lst[0] = 5
print('After Modify -', lst, '-', id(lst))

lst.append(500)
print('After Append -', lst, '-', id(lst))

lst.insert(0, 'perl')
print('After Insert -', lst, '-', id(lst))

lst.extend(['php', 'perl', 'python'])
print('After Extend -', lst, '-', id(lst))

lst.append(['php', 'perl', 'python'])
print('After Append -', lst, '-', id(lst))

tup = (1, 2, 3, 4, 5)
print(tup, '-', id(tup))
#tup[0] = 100

tup = tup + (6, 7, 8, 9, 10)
print('After Concat -', tup, '-', id(tup))

print('-' * 75)

# Membership operator (in, not in)
string = 'python'
print('Is on present in python -', 'on' in string)

print('-' * 75)

# Identity operator (is, is not)
lst_a = ['php']
lst_b = lst_a[:]

lst_a.append('python')

print('List A -', lst_a, '-', id(lst_a))
print('List B -', lst_b, '-', id(lst_b))
print('Check Ref -', lst_a is lst_b)

print('-' * 75)

num1 = 5
num2 = num1
num3 = 5

print(id(num1), '-', id(num2), '-', id(num3))

num1 = 1
print(id(num1), '-', id(num2), '-', id(num3))

print('-' * 50)

print([1, 2] * 300)

print('-' * 50)

# IF ELSE
num = 501
if num % 5 == 0:
    print('S1')
    print('S2')
    print('S3')
else:
    print('S4')
    print('S5')

print('-' * 50)

# Single Line IF ELSE
string = 'python'
is_palin = 'Yes' if string == string[::-1] else 'No'
print('Is Palin -', is_palin)

print('-' * 50)

# For loop
lst = ['php', 'perl', 'python']
for elem in lst:
    if elem == 'perl':
        break
    
    print('Element -', elem)
else:
    print('For Loop Done')

print('-' * 50)

# For loop
lst = ['php', 'perl', 'python']
for elem in lst:
    if elem == 'perl':
        break
    
    print('Element -', elem)

print('For Loop Done')

print('-' * 50)

sqr = []
for n in range(1, 11):
    if n % 3 == 0 or n % 5 == 0:
        sqr.append(n ** 2)
print('SQR -', sqr)

print('-' * 50)

# List Comprehension
sqr = [(n, n ** 2, n ** 3) for n in range(1, 11) if n % 3 == 0 or n % 5 == 0]
print('SQR LC -', sqr)

print('-' * 50)

# Dictionary Comprehension
sqr = {n: (n ** 2, n ** 3) for n in range(1, 11) if n % 3 == 0 or n % 5 == 0}
print('SQR DC -', sqr)

print('-' * 50)

# List of 50 empty dictionaries
lst = []
for n in range(1, 51):
    lst.append({})
print('List -', lst)

lst = [{} for n in range(1, 51)]
print('List -', lst)

print('-' * 50)

# Functions
def display_emp(name, loc='blr', sal=2500):
    return f'{name.upper()} from {loc.title()} earns Rs.{sal * 2}'

# Positional
print(display_emp('justin', 'blr', 5000))
# print(display_emp('blr', 5000, 'justin'))

# Keyword
print(display_emp(name='tris', loc='chennai', sal=6000))
print(display_emp(loc='chennai', sal=6000, name='tris'))

# Positional followed by keyword
print(display_emp('clark', sal=7000, loc='mumbai'))

# Default
# Non-default parameters followed by default parameters
print(display_emp('paul'))
print(display_emp('paul', sal=15000))

# Variable Length Parameters
# *args => 'n' number of positional params => tuple
# **kwargs => 'n' number of keyword params => dictionary
def display_det(*scr, **det):
    print(scr, '-', type(scr))
    print(det, '-', type(det))

display_det('python', 'perl', 'php', name='scripting', typ='interpreted')
display_det('python', name='scripting', typ='interpreted')
display_det(name='scripting', typ='interpreted')
display_det('python')

print('-' * 50)
