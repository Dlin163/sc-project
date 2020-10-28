"""
File: weather_master.py
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -1


def main():
	"""
	The program is designed to find the highest, lowest an and average
	temperature, as well as how many days wold be mark as "Low temperature
	alarm" from which the user dialed in.
	"""
	print('stanCode "Weather Master 4.0"!')
	new = int(input('Next Temperature: (or '+str(EXIT)+' to quit)?'))
	if new != EXIT:
		high = new					# When only one data
		low = new					# data = high = low = average
		number = 1
		ave = new
		if new < 16:
			c_number = 1
		else:
			c_number = 0
		while True:
			new = int(input('Next Temperature: (or '+str(EXIT)+' to quit)?'))
			if new != EXIT:
				number += 1					 # number+=1 can not be put inside average_t()
				high = compare_h(new, high)  # or the "number" could not increment.
				low = compare_l(new, low)
				ave = average_t(ave, number, new)
				c_number = cold_d(c_number, new)
			else:
				break
		print('Highest temperature = '+str(high))
		print('Lowest temperature = '+str(low))
		print('Average = ' + str(float(ave)))
		print(str(c_number)+' cold days(s)')
	else:
		print('No temperature were entered.')


def compare_h(new, high):
	"""
	Compare the latest temperature with the highest temperature.
	If higher, replace it. If not, remain the same.

	:param new: Integer, new!=EXIT, The lasted temperature input
	:param high: Integer, high!=EXIT, the highest temperature of all time
	:return: high
	"""
	if new > high:
		high = new
		return high
	else:
		high += 0
		return high


def compare_l(new, low):
	"""
	Compare the latest temperature with the lowest temperature.
	If lower, replace it. If not, remain the same.

	:param new: Integer, new!=EXIT, The lasted temperature input
	:param low: Integer, high!=EXIT, the lowest temperature of all time
	:return: low
	"""
	if new < low:
		low = new
		return low
	else:
		low += 0
		return low


def average_t(ave, number, new):
	"""
	Add up all the temperature and count average.

	:param ave: Integer, The average of all temperature before last input
	:param number: Integer, number>0. The total amount of temperature
	:param new: Integer, new!=EXIT, The lasted temperature input
	:return: ave: Integer, The current average temperature
	"""
	ave = (ave*(number-1)+new) / number
	return ave


def cold_d(c_number, new):
	"""
	To count the cold days.

	:param c_number: Integer, c_number>=0. Numbers of cold days counted
	:param new: Integer, new!=EXIT, The lasted temperature input
	:return: c_number
	"""
	if new < 16:
		c_number += 1
	else:
		c_number += 0

	return c_number


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
