"""
File: complement.py
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    This program is to find out the correspondent of the DNA.
    Which A match with T, C match with G
    """
    a = input("Please give me a DNA strand and I'll find the complement:").upper()
    b = build_complement(a)
    print('The complement of '+a+' is '+b)


def build_complement(a):
    """
    The function find out the DNA in correspondence.
    :param a: str, input by user
    :return: ans: str
    """
    ans = ''
    for i in range(len(a)):
        ch = a[i]
        if ch == 'A':
            ans += 'T'
        if ch == 'T':
            ans += 'A'
        if ch == 'G':
            ans += 'C'
        if ch == 'C':
            ans += 'G'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
