'''
Whenever any module is imported, the module (.py) file will be checked in the following directories in the same order:

a) Current Directory
b) PYTHON_HOME/lib
c) PYTHON_HOME/lib/site-packages

Temporary Fix:
Modify sys.path variable

Permanent Fix:
PYTHONPATH - environment variable
'''

import sys

print('Version of Python -', sys.version)
print('Path -', type(sys.path))

# module_dir = r'C:\THBS\Projects\Training\AI_ML_Training_July2023\Programs\modules'
# sys.path.insert(0, module_dir)

for path_name in sys.path:
    print('Path -', path_name)

import common_utils as cu
from common_utils import *

print('-' * 50)

print('Name of the Script -', __name__)

print('SQR -', cu.sqr(5))
print('Mobile Number -', validate_mobile_number('9876543210'))

print('-' * 50)

try:
    num = 501
    if num % 5 == 0:
        print('Valid Number')
    else:
        raise InvalidNumber('Number is not divisible by 5 !!!')
except InvalidNumber as e:
    print(e.display_err_msg())

print('-' * 50)
