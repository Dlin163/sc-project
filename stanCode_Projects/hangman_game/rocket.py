"""
File: rocket.py
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

SIZE = 10


def main():
    """
    This system is to construct a rocket figure in which users are able
    to manipulate to layers by inputting different 'SIZE'
    """
    a = SIZE
    head(a)
    belt(a)
    upper(a)
    lower(a)
    belt(a)
    head(a)


def head(a):
    """
    This function creates the rocket head.
    :param a: Positive int, a >= 1
    :return: no return. It prints out str
    """
    ans = ''
    for i in range(a):           # in charge of the rows
        for j in range(a - i):
            ans += ' '
        for j in range(i + 1):
            ans += '/'
        for j in range(i + 1):
            ans += '\\'
        for j in range(a - i):
            ans += ' '
        print(ans)
        ans = ''                 # empty the str before next line started


def belt(a):
    """
    This function creates the rocket belt.
    :param a: Positive int, a >= 1
    :return: no return. It prints out str
    """
    ans = '+'
    for i in range(2 * a):
        ans += '='
    ans += '+'
    print(ans)


def upper(a):
    """
    This function creates the upper part of the rocket.
    :param a: Positive int, a >= 1
    :return: no return. It prints out str
    """
    ans = '|'
    for i in range(a):
        for j in range(a-1-i):
            ans += '.'
        for j in range(i+1):
            ans += '/\\'
        for j in range(a-1-i):
            ans += '.'
        ans += '|'
        print(ans)
        ans = '|'


def lower(a):
    """
    This function creates the lower part of the rocket.
    :param a: Positive int, a >= 1
    :return: no return. It prints out str
    """

    ans = '|'
    for i in range(a):
        for j in range(i):
            ans += '.'
        for j in range(a-i):
            ans += '\\/'
        for j in range(i):
            ans += '.'
        ans += '|'
        print(ans)
        ans = '|'


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
