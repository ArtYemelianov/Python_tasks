#!/usr/bin/python3.6

import random


def parse2Int(value):
	"""
	Parses value to int

	:param value: Particular value
	:return: If parsing is success int. Otherwise None
	:rtype: int|None
	"""
	try:
		return int(value)
	except ValueError as e:
		return None

print("Hi, welcome to task one. This program offers an user predicting result of next operations.\n"
	  "If you would like to leave program input 'quit' ")

generateNewValues = False
one, two = random.randint(-100, 100), random.randint(-100, 100)
while True:
	if generateNewValues:
		one, two = random.randint(-100, 100), random.randint(-100, 100)
	true_result = one+two
	two_str = "(%d)" % two if two < 0 else str(two)
	result = input("What is result of operation '%d + %s = ?' \t" % (one, two_str))
	if not result or result == '':
		print("Your answer is empty. Please try again!")
	elif result== 'quit':
		print("Good luck!")
		break
	elif not parse2Int(result) :
		print("Your answer cannot be converted to int. Please try again!")
	elif parse2Int(result) == true_result:
		generateNewValues = True
		print("Сongratulations!!! You answered right. Try again!")
	else:
		generateNewValues = False
		print("Unfortunately, you answerd wrong. Try again!")


