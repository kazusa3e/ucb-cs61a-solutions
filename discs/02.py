# Q1: Call Diagram
#
#   Global:
#       double  --->    function double(x) [parent=Global]
#       hmmm    --->    function double(x) [parent=Global]
#           ===> NOTICE: new frame is created
#           f1:double [parent=Global]
#               x       --->    3
#             <return>  --->    6
#       wow     --->    6
#           ===> NOTICE: new frame is created
#           f2:double [parent=Global]
#                x       --->    6
#              <return>  --->    12

# Q2: Nested Calls Diagrams
#
#   Global:
#       f   --->    function f(x) [parent=Global] (x)
#       g   --->    function g(x, y) [parent=Global]
#       x   --->    3 (x)
#           ===> NOTICE: new frame is created
#           f1: g [parent=Global]
#               x   --->    f(x) [parent=Global]
#               y   --->    3
#                   ===> NOTICE: new frame is created
#                   f2: f [parent=Global]
#                             x       --->    3
#                           <return>  --->    3
#          <return> --->  False
#       x   --->    False (updated)
#           ===> NOTICE: new frame is created
#           f3: g[parent=Global]
#               x       --->    f(x) [parent=Global]
#               y       --->    0
#                   ===> NOTICE: new frame is created
#                   f4: f[parent=Global]
#                        x       --->    0
#                     <return>   --->    0
#           <return> --->    0
#       f   --->    0 (updated)

# Q3: Lambda the Environment Diagram
#
#   Global:
#       a   --->    function lambda(x) [parent=Global]
#       b   --->    function b(b, x) [parent=Global]
#       x   --->    3 (x)
#           ===> NOTICE: new frame is created
#           f1: b(b, x) [parent=Global]
#               b       --->    function lambda(x) [parent=Global]
#               x       --->    3
#               ===> NOTICE: new frame is created
#               f2: lambda(x) [parent=Global]
#                   x       --->    3
#                 <return>  --->    7
#               ===> NOTICE: new frame is created
#               f3: lambda(x) [parent=Global]
#                   x       --->    10
#                 <return>  --->    21
#            <return>   --->    21
#       x   --->    21 (updated)

# Q4: Make Adder
#
#   Global:
#       n       --->        9
#   make_adder  --->    function make_adder(n) [parent=Global]
#       ===> NOTICE: new frame is created
#       f1: make_adder(n) [parent=Global]
#           n       --->    10
#        <return>   --->    function lambda(k) [parent=f1]
#     add_ten   --->    function lambda(k) [parent=f1]
#       ===> NOTICE: new frame is created
#       f2: lambda(k) [parent=f1]
#           k       --->    9
#        <return>   --->    19
#   result      --->        19

# Q5: Make Keeper
def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out all
    integers 1..i..n where calling cond(i) returns True.
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """

    def helper(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1

    return helper


# Q6: Curry2 Diagram
#
# Global:
#   curry2      --->    function curry2(h) [parent=Global]
#       ===> NOTICE: new frame is created
#       f1: curry2(h) [parent=Global]
#           h       --->    function lambda(x, y) [parent=Global]
#           f       --->    function f(x) [parent=f1]
#        <return>   --->    function f(x) [parent=f1]
#   make_adder  --->    function f(x) [parent=f1]
#       ===> NOTICE: new frame is created
#       f2: f(x) [parent=f1]
#           x       --->    3
#           g       --->    function g(y) [parent=f2]
#        <return>   --->    function g(y) [parent=f2]
#   add_three   --->    function g(y) [parent=f2]
#       ===> NOTICE: new frame is created
#       f3: f(x) [parent=f1]
#           x       --->    4
#           g       --->    function g(y) [parent=f3]
#        <return>   --->    function g(y) [parent=f3]
#   add_four    --->    function g(y) [parent=f3]
#       ===> NOTICE: new frame is created
#       f4: g(y) [parent=f2]
#           y       --->    2
#           ===> NOTICE: new frame is created
#           f5: function lambda(x, y) [parent=Global]
#               x       --->    3
#               y       --->    2
#            <return>   --->    5
#        <return>   --->    5
#   five        --->    5

# Q7: HOF Diagram Practice
#
#   Global:
#       n       --->        7
#       f       --->        function f(x) [parent=Global] (x)
#       g       --->        function g(x) [parent=Global] (x)
#       f       --->        function f(f, x) [parent=Global] (updated)
#       ===> NOTICE: new frame is created
#       f1: f(f, x) [parent=Global]
#           f       --->    function g(x) [parent=Global]
#           x       --->    7
#           ===> NOTICE: new frame is created
#           f2: g(x) [parent=Global]
#               x       --->        14
#               n       --->        9
#               h       --->        function h() [parent=f2]
#            <return>   --->        function h() [parent=f2]
#        <return>   --->    function h() [parent=f2]
#       ===> NOTICE: new frame is created
#       f3: lambda(y) [parent=Global]
#           y       --->    function h() [parent=f2]
#           ===> NOTICE: new frame is created
#           f4 h [parent=f2]
#               <return>    --->    15
#        <return>   --->    15
#       g       --->        15 (updated)

# Q8: Match Marker
def match_k(k):
    """Return a function that checks if digits k apart match

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """

    def all_equals(arr):
        """
        >>> all_equals([1, 1, 1])
        True
        >>> all_equals([1, 2, 1])
        False
        """
        assert len(arr) > 0
        return all(map(lambda x: x == arr[0], arr))

    def get_i_column_digits(x, k, i):
        """
        >>> get_i_column_digits(123123, 3, 0)
        [3, 3]
        >>> get_i_column_digits(123123, 2, 1)
        [2, 3, 1]
        """
        result = []
        while x != 0:
            result.append((x // (10**i)) % 10)
            x = x // (10**k)
        return result

    def helper(x):
        cols = [get_i_column_digits(x, k, i) for i in range(k)]
        return all([all_equals(col) for col in cols])
        # TODO: reference solution

    return helper


def test():
    from doctest import testmod

    testmod()


if __name__ == '__main__':
    test()
