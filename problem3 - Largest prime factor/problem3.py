from math import sqrt, floor

def is_divisable(dividend, divisor):
	return dividend % divisor == 0

def is_prime(number):
	for i in range(2, floor(sqrt(number))+1 ):
		if is_divisable(number, i):
			return False
	return True

target = 600851475143
limit_divisor = floor(sqrt(target))
prime_factors = []

for n in range(2, limit_divisor+1 ):
	if is_divisable(target, n):
		if is_prime(n):
			prime_factors += [n]

print(max(prime_factors))
