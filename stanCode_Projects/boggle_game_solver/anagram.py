"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

vocab_list = []
ans_lst = []
switch = True

def main():
    s = input('Find anagrams for:').lower()
    read_dictionary(FILE)
    find_anagrams(s)


def read_dictionary(file):
    global vocab_list
    with open(file, 'r') as f:
        for line in f:
            vocab_list.append(line[0: len(line)-1])


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    find_anagrams_helper(s, '', [])
    print(f'{len(ans_lst)} anagrams: {ans_lst}')


def find_anagrams_helper(s, word, word_index):
    global vocab_list, switch
    if len(word) == len(s):
        if switch is True:
            print('Searching...')
            switch = False
        if word in vocab_list and word not in ans_lst:
            print(word)
            switch = True
            ans_lst.append(word)
    else:
        if has_prefix(word):                        # 字典裡有此開頭
            for i in range(len(s)):
                if str(i) not in word_index:        # 字元沒有重複被使用（用index看）
                    # choose
                    word_index.append(str(i))
                    word += s[i]
                    # search
                    find_anagrams_helper(s, word, word_index)
                    # un-choose
                    word_index.pop()
                    word = word[:len(word)-1]


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    global vocab_list
    tempo_vocab_list =[]
    for word in vocab_list:
        if word.startswith(sub_s):
            return True
    return False


{'apple', }
if __name__ == '__main__':
    main()
