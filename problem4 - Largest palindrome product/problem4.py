import numpy as np

palindromes = []

def is_palindrome(number):
	number_str = str(number)
	number_str_rev = ''.join(reversed(number_str))
	return number_str == number_str_rev

for num1 in range(100, 1000):
	for num2 in range(100,1000):
		product = num1 * num2
		if is_palindrome(product):
			palindromes.append(product)

#print(palindromes)
print(max(palindromes))