# Q1: Count Stair Ways
def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of n stairs, moving
    either 1 step or 2 steps at a time.

    >>> count_stair_ways(4)
    5
    """
    if n == 1 or n == 2:
        return n
    return count_stair_ways(n - 1) + count_stair_ways(n - 2)


# Q2: Count K
def count_k(n, k):
    """Counts the number of paths up a flight of n stairs when taking up to and
    including k steps at a time.

    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 1 or n == 0:
        return 1
    if k == 1:
        return 1
    if k > n:
        return count_k(n, n)
    return sum([count_k(n - x, k) for x in range(1, k + 1)])


# Q3: WWPD: Lists
def q3():
    """
    >>> a = [1, 5, 4, [2, 3], 3]
    >>> print(a[0], a[-1])
    1 3
    >>> len(a)
    5
    >>> 2 in a
    False
    >>> a[3][0]
    2
    """


# Q4: Eve weighted
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[x] * x for x in range(len(s)) if x % 2 == 0]


# Q5: Max Product
def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.

    >>> max_product([10, 3, 1, 9, 2]) # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if s == []:
        return 1
    if len(s) <= 2:
        return max(s)
    with_first = s[0] * max_product(s[2:])
    without_first = max_product(s[1:])
    return max(with_first, without_first)


def test():
    from doctest import testmod

    testmod()


if __name__ == '__main__':
    test()
