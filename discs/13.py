import re

# Q1: Greetings
def greetings(message):
    """
    Returns whether a string is a greeting. Greetings begin with either Hi,
    Hello, or Hey (first letter either capitalized or lowercase), and/or end
    with Bye (first letter either capitalized or lowercase) optionally followed
    by an exclamation point or period.

    >>> greetings("Hi! Let's talk about our favorite submissions to the Scheme Art Contest")
    True
    >>> greetings("Hey I love Taco Bell")
    True
    >>> greetings("I'm going to watch the sun set from the top of the Campanile! Bye!")
    True
    >>> greetings("Bye Bye Birdie is one of my favorite musicals.")
    False
    >>> greetings("High in the hills of Berkeley lived a legendary creature. His name was Oski")
    False
    >>> greetings('Hi!')
    True
    >>> greetings("bye")
    True
    """
    return bool(re.search(r'(^[Hh](i|ello|ey)[!]?\b)|([B|b]ye[!.]?$)', message))


# Q2: Basic URL Validation
def match_url(text):
    """

    >>> match_url("https://cs61a.org/resources/#regular-expressions")
    True
    >>> match_url("https://pythontutor.com/composingprograms.html")
    True
    >>> match_url("https://pythontutor.com/should/not.match.this")
    False
    >>> match_url("https://link.com/nor.this/")
    False
    >>> match_url("http://insecure.net")
    True
    >>> match_url("htp://domain.org")
    False
    """
    scheme = r'^((http|https)://)?'
    domain = r'([0-9a-zA-Z-.]+)'
    path = r'(/(/[0-9a-zA-Z]+)*(([0-9a-zA-Z]+.[0-9a-zA-Z]+)|([0-9a-zA-Z]+/)))?'
    anchor = r'(#[0-9a-zA-Z-]+)?$'
    full_string = scheme + domain + path + anchor
    return bool(re.match(full_string, text))


# Q3: Calculator BNF

# Will the following expressions be parsable according to this grammar?
#
# (+ 1 2)       =>          T
# (+)           =>          T
# (1)           =>          F
# (+ 1 2 3)     =>          T
# (+ 1)         =>          T
# (1 + 2)       =>          F
# (+ 1 (+ 2 3)) =>          T
# (+ 1 - 2 3)   =>          F

# Which line of the BNF should we modify to add support for calculations using a
# modulus operator, like (% 15 5)?
#
# line 4, update to:
# OPERATOR: "+" | "-" | "*" | "/" | "%"

# Does the BNF grammar provide enough information to create a working iterpreter
# for this version of the Calculator language?
#
# No. BNF can NOT eval a expression or apply a procedure.

# Q4: lambda BNF
# Omitted.

# Q5: Simple CSV
# ?start: lines
# lines: line ("\n" line)* "\n"?
# line: word ("," word)*
# word: WORD?
#
# %import common.WORD


def test():
    from doctest import testmod

    testmod()


if __name__ == '__main__':
    test()
