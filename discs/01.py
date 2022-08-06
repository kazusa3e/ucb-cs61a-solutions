# Q1: Case Conundrum
def special_case():
    x = 10
    if x > 0:
        x += 2
    elif x < 13:
        x += 3
    elif x % 2 == 1:
        x += 4
    return x  # expect 12


assert special_case() == 12


def just_in_case():
    x = 10
    if x > 0:
        x += 2
    if x < 13:
        x += 3
    if x % 2 == 1:
        x += 4
    return x  # expect 19


assert just_in_case() == 19


def case_in_point():
    x = 10
    if x > 0:
        return x + 2  # expect 12
    if x < 13:
        return x + 3
    if x % 2 == 1:
        return x


assert case_in_point() == 12

# Q2: Jacket Weather?
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    return temp < 60 or raining


# Q3: If Function vs Statement
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and false_result
    otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3 == 2, 'equal', 'not equal')
    'not equal'
    >>> if_function(3 > 2, 'bigger', 'smaller')
    'bigger'
    """
    return true_result if condition else false_result


def with_if_statement():
    """
    >>> result = with_if_statement()
    61A
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()


def with_if_function():
    """
    >>> result = with_if_function()
    Welcome to
    61A
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func())


def cond():
    return 0


def true_func():
    print('Welcome to')


def false_func():
    print('61A')


# Q4: Square So Slow


def square(x):
    print('here!')
    return x * x


def so_slow(num):
    x = num
    while x > 0:
        x = x + 1  # NOTICE: infinite loop here
    return x / 0


# square(so_slow(5))

# Q5: Is Prime?
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    assert n > 1
    return all([n % x != 0 for x in range(2, n)])


# Q6: Fizzbuzz
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result is None  # No return value
    True
    """
    i = 0
    while i < n:
        i += 1
        if i % 15 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)


# Q7: Assignment Diagram
#
#   x   --->    3 (x)
#   y   --->    3
#   x   --->    9 (updated)


# Q8: def Diagram
#
#  double   --->    function double(x) [parent=Global] (x)
#  triple   --->    function triple(x) [parent=Global]
#  hat      --->    function double(x) [parent=Global]
#  double   --->    function double(x) [parent=Global] (updated)


def test():
    from doctest import testmod

    testmod()


if __name__ == '__main__':
    test()
