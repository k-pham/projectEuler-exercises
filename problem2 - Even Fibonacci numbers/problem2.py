# sum of even fibonacci numbers below 4 million

#import numpy as np
limit = 4000000

list_of_fibonacci = [ 1, 2 ]
while list_of_fibonacci[-1] <= limit:
	list_of_fibonacci.append( list_of_fibonacci[-1] + list_of_fibonacci[-2] )
	assert list_of_fibonacci[-1] > list_of_fibonacci[-2]

assert list_of_fibonacci[-1] > limit
print("Just computed", len(list_of_fibonacci), "Fibonacci numbers")
print("Last Fibonacci number computed was", list_of_fibonacci[-1])

even_fibonacci = [x for x in list_of_fibonacci if x % 2 == 0]
print(even_fibonacci)

# alternative way of getting even number
# assumes knowledge that every 3rd number starting on the second is even
even_test = list_of_fibonacci[1::3]
print(even_test)
#print("Alternative way worked?", even_test == even_fibonacci)
if even_test == even_fibonacci:
	print("Yay! Alternative way worked")

print("Sum of even Fibonacci numbers that do not exceed four million", sum(even_fibonacci))