__all__ = ['validate_mobile_number', 'InvalidNumber']

# Find the square of first 'n' numbers
sqr = lambda n: [x ** 2 for x in range(1, n + 1)]

# Function
def validate_mobile_number(mobile):
    status = 'invalid'

    if len(mobile) == 10 and mobile.isdigit() and int(mobile[0]) in range(5, 10):
        status = 'valid'

    return mobile, status

# User Defined Exception
class InvalidNumber(Exception):
    def __init__(self, err_msg):
        self.err_msg = err_msg

    def display_err_msg(self):
        return f'Exception Occurred: {self.err_msg}'

if __name__ == '__main__':
    print('-' * 50)
    print('Name of the Module -', __name__)
    print('SQR of 10 Nos -', sqr(10))
    print('-' * 50)
