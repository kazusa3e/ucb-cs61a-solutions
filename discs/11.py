# Q1: Is Tail Call
# (define (question-a x) (        ; F
#     if (= x 0) 0
#         (+ x (question-a (- x 1)))
# ))

# (define (question-b x y) (      ; T
#     if (= x 0) y
#         (question-b (- x 1) (+ y x))
# ))

# (define (question-c x y) (      ; T
#     if (> x y)
#         (question-c (- y 1) x)
#         (question-c (+ x 10) y)
# ))

# (define (question-d n) (        ; T
#     if (question-d n)
#         (question-d (- n 1))
#         (question-d (+ n 10))
# ))

# (define (question-e n) (        ; T
#     cond
#         ((<= n 1) 1)
#         ((question-e (- n 1)) (question-e (- n 2)))
#         (else (begin (print 2) (question-e (- n 3))))
# ))

# Q2: Sum
# (define (sum lst) (
#     define (sum-iter l s) (
#         if (null? l)
#             s
#             (sum-iter (cdr l) (+ s (car l)))
#     ))
#     (sum-iter lst 0)
# )

# (expect (sum '(1 2 3)) 6)
# (expect (sum '(10 -3 4)) 11)

# Q3: Reverse
# (define (reverse lst) (
#         define (reverse-iter l r) (
#             if (null? l)
#                 r
#                 (reverse-iter (cdr l) (cons (car l) r))
#         )
#     )
#     (reverse-iter lst nil)
# )

# (expect (reverse '(1 2 3)) (3 2 1))
# (expect (reverse '(0 9 1 2)) (2 1 9 0))

# Q4: Using Pair
def scheme_valid_cdrp(pair):
    return True


class SchemeError(Exception):
    pass


class Pair:
    """Represents the built-in pair data structure in Scheme."""

    def __init__(self, first, rest):
        self.first = first
        if not scheme_valid_cdrp(rest):
            raise SchemeError(
                'cdr can only be a pair, nil, or a promise but was {}'.format(rest),
            )
        self.rest = rest

    def map(self, fn):
        """Maps fn to every element in a list, returning a new Pair.

        >>> Pair(1, Pair(2, Pair(3, nil))).map(lambda x: x * x)
        Pair(1, Pair(4, Pair(9, nil)))
        """
        assert (
            isinstance(self.rest, Pair) or self.rest is nil
        ), 'rest element in pair must be another pair or nil'
        return Pair(fn(self.first), self.rest.map(fn))

    def __repr__(self):
        return 'Pair({}, {})'.format(self.first, self.rest)


class nil:
    """Represents the special empty pair nil in Scheme."""

    def map(self, fn):
        return nil

    def __getitem__(self, i):
        return IndexError('Index out of range')

    def __repr__(self):
        return 'nil'


nil = nil()

# Write out the Python expression that returns a pair representing the given
# expression:
Pair('+', Pair(Pair('-', Pair(2, Pair(4, nil))), Pair(6, Pair(8, nil))))

# What is the operator of the call expression?
'+'

# If the Pair you constructed in the previous part was bound to name p, how
# would you retrieve the operator?
p = Pair('+', Pair(Pair('-', Pair(2, Pair(4, nil))), Pair(6, Pair(8, nil))))
operator = p.first

#  What are the operands of the call expression?
operand1 = Pair('-', Pair(2, Pair(4, nil)))
operand2 = 6
operand3 = 8

# If the Pair you constructed was bound to the name p, how would you retrieve a
# list containing all of the operands?
operands_list = p.rest

# How would you retrieve only the first operand?
first_operand = p.rest.first

# Q5: New Procedure
def calc_apply(operator, operands):
    return operator(operands)


def calc_eval(exp):
    if isinstance(exp, Pair):  # Call expressions
        return calc_apply(calc_eval(exp.first), exp.rest.map(calc_eval))
    elif exp in OPERATORS:  # Names
        return OPERATORS[exp]
    else:
        return exp


def floor_div(expr):
    """
    # >>> calc_eval(Pair('//', Pair(10, Pair(10, nil))))
    # 1
    # >>> calc_eval(Pair('//', Pair(20, Pair(2, Pair(5, nil)))))
    # 2
    # >>> calc_eval(Pair('//', Pair(6, Pair(2, nil))))
    # 3
    >>> calc_eval(Pair('//', Pair(6, Pair(Pair('//', Pair(20, Pair(2, Pair(5, nil)))), nil))))
    3
    """
    dividend, divisors = expr.first, expr.rest
    while divisors is not nil:
        dividend = dividend // divisors.first
        divisors = divisors.rest
    return dividend


OPERATORS = {'//': floor_div}

# Also for this question do you need to call calc_eval inside floor_div? Why or
# why not?

# No.

# Q6: New Form

# Are we able to handle expressions containing the comparison operators (such as
# <. >. or =) with the existing implementation of calc_eval? Why or why not?

# Yes.

# Are we able to handle and expressions with the existing implementation of
# calc_eval? Why or why not?

# No. and expressions features the short circuit principle.

# Now, complete the implementation below to handle and expressions. You may
# assum the conditional operators (e.g. <, >, =, etc) have already been
# implemented for you.


def calc_eval(exp):
    if isinstance(exp, Pair):
        if exp.first == 'and':  # and expressions
            return eval_and(exp.rest)
        else:
            return calc_apply(calc_eval(exp.first), exp.rest.map(calc_eval))
    elif exp in OPERATORS:  # Names
        return OPERATORS[exp]
    else:
        return exp


def eval_and(operands):
    """
    >>> calc_eval(Pair('and', Pair(1, nil)))
    1
    >>> calc_eval(Pair('and', Pair(False, Pair('1', nil))))
    False
    """
    ret = True
    while operands is not nil:
        ret = operands.first if ret and operands.first else False
        operands = operands.rest
        if not ret:
            return False
    return ret


# Q7: Saving Values
bindings = {}


def calc_eval(exp):
    if isinstance(exp, Pair):
        if exp.first == 'and':  # and expressions
            return eval_and(exp.rest)
        elif exp.first == 'define':  # define expressions
            return eval_define(exp.rest)
        else:  # call expressions
            return calc_apply(calc_eval(exp.first), exp.rest.map(calc_eval))
    elif exp in bindings:  # looking up variables
        return bindings[exp]
    elif exp in OPERATORS:  # looking up procedures
        return OPERATORS[exp]
    else:
        return exp


def eval_define(expr):
    """
    >>> calc_eval(Pair('define', Pair('a', Pair(1, nil))))
    'a'
    >>> calc_eval('a')
    1
    """
    if expr.rest is nil:
        return bindings[expr.first]
    bindings[expr.first] = expr.rest.first
    return expr.first


# Q8: Counting Eval and Apply


def add(expr):
    sum, val = expr.first, expr.rest
    while val is not nil:
        sum += val.first
        val = val.rest
    return sum


OPERATORS['+'] = add


def counted(procedure):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return procedure(*args, **kwargs)

    wrapper.call_count = 0
    return wrapper


# How many calls to calc_eval and calc_apply would it take to evaluate each of
# the following Calculator expressions?
calc_eval = counted(calc_eval)
calc_apply = counted(calc_apply)
calc_eval(Pair('+', Pair(1, Pair(2, nil))))
assert calc_eval.call_count, 4
assert calc_apply.call_count, 0

# For this particular prompt please list out the inputs to calc_eval and
# calc_apply.

# TODO:

# Q9: From Pair to Calculator
Pair('+', Pair(1, Pair(2, Pair(3, Pair(4, nil)))))
# (+ 1 2 3 4)

Pair('+', Pair(1, Pair(Pair('*', Pair(2, Pair(3, nil))), nil)))
# (+ 1 (* 2 3))


def test():
    from doctest import testmod

    testmod()


if __name__ == '__main__':
    test()
