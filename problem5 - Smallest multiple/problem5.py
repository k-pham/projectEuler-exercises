# Smallest multiple of 1 to 20

def is_divisable(dividend, divisor):
	return dividend % divisor == 0

target = 20
found = False
testnumb = 0

while found == False:
	testnumb += target*(target-1)
	for divisor in range(1,target):
		if is_divisable(testnumb, divisor) == False:
			break
	else:
		print('Smallest multiple of 1 to ', target,' is ',testnumb)
		found = True