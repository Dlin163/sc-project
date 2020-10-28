"""
File: caesar.py
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    The program is meant to decipher the code in which the user typed.
    """
    shift = int(input('Secret number:'))
    cipher = input('Whats the cipher string?').upper()
    org = ALPHABET                                      # Just personal preference
    new = compose(shift, org)
    decipher = compare(new, org, cipher)
    print('The deciphered string is: '+decipher)


def compose(shift, org):
    """
    Compose the new string correspond to org.

    :param shift: int, shift > 0. How many span needed to be shifted
    :param org:str, original string
    :return: new, str
    """
    frag_1 = org[:len(org)-shift]
    frag_2 = org[len(org)-shift:]
    new = frag_2 + frag_1
    return new


def compare(new, org, cipher):
    """
    The function finds out the correspondent by 3-way comparing
    cipher, new string and original string.

    :param new: str, new string
    :param org: str, original string
    :param cipher: str, code users entered
    :return: decipher: str, correspondent of the code
    """
    decipher = ''
    for i in range(len(cipher)):
        position = new.find(cipher[i])  # Just a rephrase to make it clear
        if position != -1:              # Make sure its legal(not blanks or punctuation)
            decipher += org[position]
        else:
            decipher += cipher[i]       # Making sure blanks or punctuation will be add.
    return decipher


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
