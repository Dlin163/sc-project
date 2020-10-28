"""
File: hangman.py
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    This program is built for matching user's guessing with the answer.
    There will be only "N_TURNS" chances available.
    """
    guess_n = N_TURNS               # To compare how many guesses user had and have.
    word = random_word()            # enable us to acknowledge which hangman pic to show
    intro(guess_n, word)
    match(word, guess_n)


def random_word():
    """
    Pick a word by computer randomly .

    :return: one of the str below
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def intro(guess_n, word):
    """
    Show the introduction of the program

    :param guess_n: int, guess_n >= 0. Total guessing number available
    :param word: str, random word chosen
    :return: Print out instructions
    """
    print('The word looks like:', end='')
    for i in range(len(word)):
        print('-', end='')
    print('')
    print('You have '+str(guess_n)+' guesses left')


def match(word, guess_n):
    """
    This function is built for matching user's guessing with the answer.
    Every single alpha will be scrutinized.
    If correct, alpha will be shown to users and replace '-'.
    If not, guessing chances will depreciate.
    (it will print illegal if user type in alpha from dictionary or guesses two alphas at once)

    :param word: str, Random word computer chosen
    :param guess_n: int, guess_n >= 0. Total guessing number available
    :return: Print out correct or wrong to user
    """
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'                         # As a dictionary. To check guesses legal or not
    ans = ''
    for i in range(len(word)):                                   # Build a str of same length as answer to be replaced
        ans += '-'

    while ans.find('-') != -1:                                   # When exist '-'. The word is not completely guessed
        if guess_n != 0:                                         # Make sure guesses(chance) are available
            guess = str(input('Your guess:')).upper()
            if alpha.find(guess) != -1:                          # Make sure alpha guessed is legal
                if word.find(guess) != -1:                       # To see alpha guessed is correct or not
                    for i in range(len(word)):                   # Search every alpha.Prevent re-shown alpha
                        if word[i] == guess:
                            ans = ans[:i] + guess + ans[i+1:]    # Replace '-' with right alpha
                    if ans.find('-') != -1:
                        print_pic(guess_n, N_TURNS)
                        print('You are correct!')
                        print('The word looks like '+ans)
                        print('You have ' + str(guess_n) + ' left.')
                else:
                    guess_n -= 1
                    print_pic(guess_n, N_TURNS)
                    print('There is no '+guess+"'s in the word.")
                    if guess_n != 0:
                        print('The word looks like ' + ans)
                        print('You have '+str(guess_n)+' guesses left')
            else:
                print_pic(guess_n, N_TURNS)
                print('illegal format.')
        else:
            print('You are completely hung : (')
            print('The word was: ' + word)
            break

    else:
        print_pic(guess_n, N_TURNS)
        print('You are correct!')
        print('You win!!')
        print('The word was: '+word)


def print_pic(guess_n, N_TURNS):
    """
    To print out the hangman when users guess an alpha.

    :param guess_n: int, guess_n >= 0. Total guessing number available
    :param N_TURNS: int, guess_n >= 0. Total guessing available initially
    :return: Print out hangman pic
    """
    s1 = '  一 一'
    s2 = ' |    |'
    s3 = ' |    '
    s4 = ' |   '
    s5 = ' |   '
    s6 = '_|_    '
    if guess_n == N_TURNS:
        print(s1)
        print(s2)
        print(s3)
        print(s4)
        print(s5)
        print(s6)
    elif guess_n == N_TURNS - 1:
        print(s1)
        print(s2)
        print(s3 + 'O')
        print(s4)
        print(s5)
        print(s6)
    elif guess_n == N_TURNS - 2:
        print(s1)
        print(s2)
        print(s3 + 'O')
        print(s4 + ' |')
        print(s5)
        print(s6)
    elif guess_n == N_TURNS - 3:
        print(s1)
        print(s2)
        print(s3 + 'O')
        print(s4 + '/|')
        print(s5)
        print(s6)
    elif guess_n == N_TURNS - 4:
        print(s1)
        print(s2)
        print(s3 + 'O')
        print(s4 + '/|\\')
        print(s5)
        print(s6)
    elif guess_n == N_TURNS - 5:
        print(s1)
        print(s2)
        print(s3 + 'O')
        print(s4 + '/|\\')
        print(s5 + '/')
        print(s6)
    elif guess_n == N_TURNS - 6:
        print(s1)
        print(s2)
        print(s3 + 'O')
        print(s4 + '/|\\')
        print(s5 + '/ \\')
        print(s6)
    else:
        print(s1)
        print(s2)
        print(s3 + 'Q')
        print(s4 + '/|\\')
        print(s5 + '/ \\')
        print(s6)



#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
