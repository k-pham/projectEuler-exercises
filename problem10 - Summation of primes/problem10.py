from math import sqrt, floor

def is_divisable(dividend, divisor):
	return dividend % divisor == 0

def is_prime(number):
	for i in range(2, floor(sqrt(number))+1 ):
		if is_divisable(number, i):
			return False
	return True