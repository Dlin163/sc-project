"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
ALPHA = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

dictionary_list = []
dictionary_dic = {}
current =''
answer = []



def main():
	line1 = input_rows(1)
	line2 = input_rows(2)
	line3 = input_rows(3)
	line4 = input_rows(4)
	word_matrix = [line1, line2, line3, line4]
	check_matrix = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
	read_dictionary()
	for y in range(len(word_matrix)):
		for x in range(4):
			start_alpha = word_matrix[y][x]
			check_matrix[y][x] = start_alpha
			search(start_alpha, word_matrix, check_matrix, x, y, [])


def search(word, word_matrix, check_matrix, w_x, w_y, choosen_positions):

	if len(word) >= 4 and word in dictionary_dic and word not in answer:
		answer.append(word)
		print('Found \"' + word + '\"')
	for y in range(-1, 2):
		for x in range(-1, 2):
			# inside the matrix
			if 0 <= w_x + x < 4 and 0 <= w_y + y < 4:
				if (w_x + x, w_y + y) not in choosen_positions:
					# (choose)
					word += word_matrix[w_y + y][w_x + x]
					choosen_positions.append((w_x + x, w_y + y))

					# (search) if it is not in check_matrix means unused
					search(word, word_matrix, check_matrix, w_x+x, w_y+y, choosen_positions)
					# (un-choose)
					word = word[:len(word)-1]
					choosen_positions.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			dictionary_list.append(line[:len(line) - 1])
			dictionary_dic[line[:len(line) - 1]] = line[:len(line) - 1]


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary_list:
		if word.startswith(sub_s):
			return True
	return False


def input_rows(row_num):
	letter = 0
	while True:
		line = input(f'{row_num} row of letter:').lower().split()
		for ch in line:
			if len(ch) != 1 or len(line) != 4:
				print('Illegal Format')
				letter = 0
				break
			else:
				letter += 1
				if letter == 4:
					letter = 0
					return line


if __name__ == '__main__':
	main()
