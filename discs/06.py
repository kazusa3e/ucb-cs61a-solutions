# Q1: WWPD: Repr-esentation
class A:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return self.x

    def __str__(self):
        return self.x * 2


class B:
    def __init__(self):
        print('boo!')
        self.a = []

    def add_a(self, a):
        self.a.append(a)

    def __repr__(self):
        print(len(self.a))
        ret = ''
        for a in self.a:
            ret += str(a)
        return ret


def q1():
    """
    >>> A('one')
    one
    >>> print(A('one'))
    oneone
    >>> repr(A('two'))
    'two'
    >>> b = B()
    boo!
    >>> b.add_a(A('a'))
    >>> b.add_a(A('b'))
    >>> b
    2
    aabb
    """


# Q2: Height


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


def height(t):
    """Return the height of a tree.

    >>> t = Tree(3, [Tree(5, [Tree(1)]), Tree(2)])
    >>> height(t)
    2
    >>> t = Tree(3, [Tree(1), Tree(2, [Tree(5, [Tree(6)]), Tree(1)])])
    >>> height(t)
    3
    """
    if t.branches == []:
        return 0
    return max([height(b) for b in t.branches]) + 1


# Q3: Maximum Path Sum
def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = Tree(1, [Tree(5, [Tree(1), Tree(3)]), Tree(10)])
    >>> max_path_sum(t)
    11
    """
    if t.branches == []:
        return t.label
    return t.label + max([max_path_sum(b) for b in t.branches])


# Q4: Find Path
def find_path(t, x):
    """
    >>> t = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)
    """
    if t.branches == []:
        return [t.label] if t.label == x else None
    for b in t.branches:
        subpath = find_path(b, x)
        if subpath:
            return [t.label, *subpath]


# Q5: Prune Small
def prune_small(t, n):
    """Prune the tree mutatively, keeping only the n branches of each node with
    the smallest label.

    >>> t1 = Tree(6)
    >>> prune_small(t1, 2)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_small(t2, 1)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2), Tree(3)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_small(t3, 2)
    >>> t3
    Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2)])])
    """
    if t.branches == []:
        return
    while len(t.branches) > n:
        t.branches.remove(max(t.branches, key=lambda node: node.label))
    for b in t.branches:
        prune_small(b, n)


def test():
    from doctest import testmod

    testmod()


if __name__ == '__main__':
    test()
