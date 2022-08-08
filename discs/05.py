# Q1: Map, Filter, Reduce
def my_map(fn, seq):
    """Applies fn onto each element in seq and returns a list.

    >>> my_map(lambda x: x * x, [1, 2, 3])
    [1, 4, 9]
    """
    return [fn(x) for x in seq]


def my_filter(pred, seq):
    """Keeps elements in seq only if they satisfy pred.

    >>> my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])
    [2, 4]
    """
    return [x for x in seq if pred(x)]


def my_reduce(combiner, seq):
    """Combines elements in seq using combiner.
    seq will have at least one element.
    >>> my_reduce(lambda x, y: x + y, [1, 2, 3, 4])
    10
    >>> my_reduce(lambda x, y: x * y, [1, 2, 3, 4])
    24
    >>> my_reduce(lambda x, y: x + 2 * y, [1, 2, 3])
    11
    """
    initial, ix = seq[0], 1
    while ix != len(seq):
        initial = combiner(initial, seq[ix])
        ix += 1
    return initial


# Q2: WWPD: Mutability
def q2():
    """
    >>> s1 = [1, 2, 3]
    >>> s2 = s1
    >>> s1 is s2
    True
    >>> s2.extend([5, 6])
    >>> s1[4]
    6
    >>> s1.append([-1, 0, 1])
    >>> s2[5]
    [-1, 0, 1]
    >>> s3 = s2[:]
    >>> s3.insert(3, s2.pop(3))
    >>> len(s1)
    5
    >>> s1[4] is s3[6]
    True
    >>> s3[s2[4][1]]
    1
    >>> s1[:3] is s2[:3]
    False
    >>> s1[:3] == s2[:3]
    True
    >>> s1[4].append(2)
    >>> s3[6][3]
    2
    """


# Q3: WWPD: Student OOP
class Student:
    max_slip_days = 3

    def __init__(self, name, staff):
        self.name = name
        self.understanding = 0
        staff.add_student(self)
        print('Added', self.name)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print('Thanks, ' + staff.name)


class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1

    def grant_more_slip_days(self, student, days):
        student.max_slip_days = days


def q3():
    """
    >>> callahan = Professor('Callahan')
    >>> elle = Student('Elle', callahan)
    Added Elle
    >>> elle.visit_office_hours(callahan)
    Thanks, Callahan
    >>> elle.visit_office_hours(Professor('Paulette'))
    Thanks, Paulette
    >>> elle.understanding
    2
    >>> [name for name in callahan.students]
    ['Elle']
    >>> x = Student('Vivian', Professor('Stromwell')).name
    Added Vivian
    >>> x
    'Vivian'
    >>> [name for name in callahan.students]
    ['Elle']
    >>> elle.max_slip_days
    3
    >>> callahan.grant_more_slip_days(elle, 7)
    >>> elle.max_slip_days
    7
    >>> Student.max_slip_days
    3
    """


# Q4: Keyboard
class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.times_pressed = 0


class Keyboard:
    """A keyboard takes in an arbitrary amount of buttons, and has a dictionary
    of positions as keys, and values as Buttons.
    >>> b1 = Button(0, 'H')
    >>> b2 = Button(1, 'I')
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.press(2)  # No button at this position
    ''
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.times_pressed
    2
    >>> b2.times_pressed
    3
    """

    def __init__(self, *args):
        self.buttons = {}
        for b in args:
            self.buttons[b.pos] = b

    def press(self, info):
        """Takes in a position of the button pressed, and returns that button's
        output."""
        if info in self.buttons.keys():
            btn = self.buttons[info]
            btn.times_pressed += 1
            return btn.key
        return ''

    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and returns the
        total output."""
        return ''.join([self.press(c) for c in typing_input])


def test():
    from doctest import testmod

    testmod()


if __name__ == '__main__':
    test()
