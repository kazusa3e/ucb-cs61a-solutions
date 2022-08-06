# Q1: Warm Up: Recursive Multiplication
def multiply(m, n):
    """Takes two positive integers and returns their product using recursion.

    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    return m + multiply(m, n - 1)


# Q2: Recursion Environment Diagram
#
#   Global:
#       rec         --->        function rec(x, y) [parent=Global]
#       ===> NOTICE: new frame is created
#       f1: rec(x, y) [parent=Global]
#           x       --->        3
#           y       --->        2
#               ===> NOTICE: new frame is created
#               f2: rec(x, y) [parent=Global]
#                   x       --->        3
#                   y       --->        1
#                   ===> NOTICE: new frame is created
#                   f3: rect(x, y) [parent=Global]
#                       x       --->        3
#                       y       --->        0
#                    <return>   --->        1
#                <return>   --->    3
#        <return>   --->        9

# Q3: Find the Bug
def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    if n == 1:  # FIX: append case n == 1
        return 1
    return n * skip_mul(n - 2)


# Q4: Recursive Hailstone
def hailstone(n):
    """Print out the hailstone sequence staring at n, and return the number of
    elements in the sequnce.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """

    def helper(n, steps):
        print(n)
        if n == 1:
            return steps
        else:
            if n % 2 == 0:
                return helper(n // 2, steps + 1)
            else:
                return helper(n * 3 + 1, steps + 1)

    return helper(n, 1)


# Q5: Merge Numbers
def merge(n1, n2):
    """Merges two number by digit in decreasing order

    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge(21, 31)
    3211
    """
    if n1 == 0 or n2 == 0:
        return abs(n1 - n2)
    if (n1 % 10) < (n2 % 10):
        return merge(n1 // 10, n2) * 10 + (n1 % 10)
    else:
        return merge(n1, n2 // 10) * 10 + (n2 % 10)


# Q6: Is Prime
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    assert n > 1

    def helper(n, i):
        if i == n:
            return True
        if n % i == 0:
            return False
        return helper(n, i + 1)

    return helper(n, 2)


def test():
    from doctest import testmod

    testmod()


if __name__ == '__main__':
    test()
