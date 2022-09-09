# Q1: Paths List
def paths(x, y):
    """Return a list of ways to reach y from x by repeated
    incrementing or doubling.
    >>> paths(3, 5)
    [[3, 4, 5]]
    >>> sorted(paths(3, 6))
    [[3, 4, 5, 6], [3, 6]]
    >>> sorted(paths(3, 9))
    [[3, 4, 5, 6, 7, 8, 9], [3, 4, 8, 9], [3, 6, 7, 8, 9]]
    >>> paths(3, 3) # No calls is a valid path
    [[3]]
    """
    if x == y:
        return [[x]]
    elif x * 2 > y:
        return [list(range(x, y + 1))]
    else:
        a = [[x] + p for p in paths(x + 1, y)]
        b = [[x] + p for p in paths(x * 2, y)]
        return a + b


# Q2: Reverse
def reverse(lst):
    """Reverses lst using mutation.

    >>> original_list = [5, -1, 29, 0]
    >>> reverse(original_list)
    >>> original_list
    [0, 29, -1, 5]
    >>> odd_list = [42, 72, -8]
    >>> reverse(odd_list)
    >>> odd_list
    [-8, 72, 42]
    """

    def helper(l, start, end):
        if end - start < 1:
            return
        l[start], l[end] = l[end], l[start]
        helper(l, start + 1, end - 1)

    helper(lst, 0, len(lst) - 1)


# Q3: Reverse Other
def reverse_other(t):
    """Mutates the tree such that nodes on every other (odd-depth) level have
    the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """

    def reverse_labels(branches):
        def helper(l, start, end):
            if end - start < 1:
                return
            l[start].label, l[end].label = l[end].label, l[start].label
            helper(l, start + 1, end - 1)

        helper(branches, 0, len(branches) - 1)

    def helper(t, d):
        if t.branches == []:
            return
        if d % 2 == 0:
            reverse_labels(t.branches)
        for b in t.branches:
            helper(b, d + 1)

    helper(t, 0)


# Q4: Multiple Links
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    from functools import reduce
    from operator import mul

    if any([lnk is Link.empty for lnk in lst_of_lnks]):
        return Link.empty
    return Link(
        reduce(mul, [lnk.first for lnk in lst_of_lnks]),
        multiply_lnks([lnk.rest for lnk in lst_of_lnks]),
    )


# Q5: Group by Non-Decreasing
#
# (define (nondecreaselist s) (
#     cond
#         ((null? s) ())
#         ((= (length s) 1) (list s))
#         (else (
#             let (
#                 (rest (nondecreaselist (cdr s)))
#             ) (
#                 if (> (car s) (car (car rest)))
#                     ; ((2 3) (1 2 3)) -> ((4) (2 3) (1 2 3))
#                     (cons (list (car s)) rest)
#                     ; ((2 3) (1 2 3)) -> ((1 2 3) (1 2 3))
#                     (cons
#                         (cons (car s) (car rest))
#                         (cdr rest)
#                     )
#             )
#         ))
# ))

# Q6: To Scheme An Environment Diagram
#
# (define lamb2 (lambda (x) (+ x y)))
# (define cow2 (mu (x) (+ x y)))
# (define y 5)
# (lamb2 1)
# (cow2 1)
#
# Q: What is the parent frame of frame f1?
# A: Global Frame
#
# Q: What is the parent frame of frame f2?
# A: Global frame
#
# (define (goat x y) (lambda (x) (+ x y)))
# (define (horse x y) (mu (x) (+ x y)))
# (define horns (goat 1 2))
# (define saddle (horse 1 2))
# (define x 10)
# (define y 20)
# (horns 5)
# (saddle 5)
# Q: Which frame is created by the call to `(goat 1 2)`, and what is the parent
# of this frame?
# A: Frame f1. The parent of frame f1 is global.
# Q: What kind of procedure is horns, and what scoping rule does it use?
# A: `horns` is a lambda procedure.
# Q: What kind of procedure is saddle, and what scoping rule does it use?
# A: `saddle` is a mu precedure.
# Q: Which frame is created by the call to (horns 5), and what is the parent of
# this frame?
# A: Frame f3. The parent of frame f3 is f1.
# Q: Which frame is created by the call to (saddle 5), and what is the parent of
# this frame?
# A: Frame f4. The parent frame of f4 is Global.
# Q: What would be the output of the lines (horns 5) and (saddle 5)?
# A: 7 and 25
# Q: Would there be any difference in output if horse was defined using a lambda
# as opposed to a define, e.g. (define horse (lambda (x y) ...))? If so, what?
# A: no...?

# Q7: Or with Multiple Args
# (define (make-long-or args)
#     (cond
#         ((null? args) #f)
#         (else
#             `(let ((v1 ,(car args)))
#                 (if v1
#                     v1
#                     ,(make-long-or (cdr args))
#                 )
#             )
#         )
#     )
# )

# Q8: Phone Number Validator
import re


def phone_number(string):
    """
    >>> phone_number("Song by Logic: 1-800-273-8255")
    True
    >>> phone_number("123 456 7890")
    True
    >>> phone_number("1" * 11) and phone_number("1" * 10) and phone_number("1" * 7)
    True
    >>> phone_number("The secret numbers are 4, 8, 15, 16, 23 and 42 (from the TV show Lost)")
    False
    >>> phone_number("Belphegor's Prime is 1000000000000066600000000000001")
    False
    >>> phone_number(" 1122334455 ")
    True
    >>> phone_number(" 11 22 33 44 55 ")
    False
    >>> phone_number("Tommy Tutone's '80s hit 867-5309 /Jenny")
    True
    >>> phone_number("11111111") # 8 digits isn't valid, has to be 11, 10, or 7
    False
    """
    return bool(
        re.search(
            r'\b((\d{3}[- ]?\d{4})|(\d{3}[- ]?\d{3}[- ]?\d{4})|(\d[- ]?\d{3}[- ]?\d{3}[- ]?\d{4}))\b',
            string,
        )
    )


# Q9: Comprehension is Everything
#
# Q: Select all of the non-terminal symbols in the grammer:
# A: comp, expression, operation
#
# Q: Which of the following comprehensions would be successfully parsed by the
# grammer?
# A:
#   - [x * 2 for x in list]
#   - [x for x in list]
#
# Q: Which line(s) would we need to modify to add support for the syntax
# described above, assuming that the conditional always compares an expression
# to a number? Now modify the selected line(s) so that it can parse the syntax
# described above.
# A:
# start: comp
# ?comp: "[" expression "for" IDENTIFIER "in" IDENTIFIER ("if" expression)? "]"
# expression: IDENTIFIER operation*
# operation: (OPERATOR | COMPARER) NUMBER
# IDENTIFIER: /[a-zA-Z]+/
# OPERATOR: "+" | "-" | "*" | "/"
# COMPARER: ">" | "<" | "==" | ">=" | "<="
#
# %import common.NUMBER
# %ignore /\s+/
#
# Q: Modify the grammar so that it can now parse nested list comprehensions.
# A:
# start: comp
# ?comp: "[" (expression | comp) "for" IDENTIFIER "in" (IDENTIFIER | comp) ("if" expression)? "]"
# expression: IDENTIFIER operation*
# operation: (OPERATOR | COMPARER) NUMBER
# IDENTIFIER: /[a-zA-Z]+/
# OPERATOR: "+" | "-" | "*" | "/"
# COMPARER: ">" | "<" | "==" | ">=" | "<="
#
# %import common.NUMBER
# %ignore /\s+/


class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)


class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


def test():
    from doctest import testmod

    testmod()


if __name__ == '__main__':
    test()
