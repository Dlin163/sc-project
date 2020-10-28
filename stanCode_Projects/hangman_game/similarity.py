"""
File: similarity.py
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program help user acquire the bio-sequence with the most precision.
    Namely, the word printed out would have the best most alphabet in common between
    long ans short sequence.
    User should only enter A, T, C, G
    """
    l_s = input('Please give me a DNA sequence to search:').upper()
    s_s = input('What DNA sequence would you like to match?').upper()
    b_s = match(l_s, s_s)
    print('The best match is '+b_s)


def match(l_s, s_s):
    """
    TO compare the long and short sequence one by one and find the most accurate one.

    :param l_s: str, long sequence where short sequence find the most similar one
    :param s_s: str, short sequence. As a standard to search
    :return: b_s
    """
    b_s = ''                                    # best sequence
    b_c_a = 0                                   # best correct alpha. Use it to compare the highest accuracy with other
    for i in range(0, len(l_s)-len(s_s)+1):     # len(l_s)-len(s_s)+1 is total number of combination
        t_s = l_s[i:len(s_s)+i]
        c_n = 0
        for j in range(len(s_s)):
            if s_s[j] == t_s[j]:
                c_n += 1
        if c_n > b_c_a:
            b_s = t_s
            b_c_a = c_n
    return b_s


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
