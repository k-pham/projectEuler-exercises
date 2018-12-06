from math import sqrt, floor

def is_divisable(dividend, divisor):
	return dividend % divisor == 0

def is_prime(number):
	for i in range(2, floor(sqrt(number))+1 ):
		if is_divisable(number, i):
			return False
	return True

primes = []
target = 10001
testnumb = 1

while len(primes) < target:
	testnumb += 1
	if is_prime(testnumb):
		primes += [testnumb]

print(len(primes))
print(primes[target-1])