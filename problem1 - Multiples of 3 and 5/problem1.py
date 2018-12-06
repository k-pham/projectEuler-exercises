# sum of multiples of 3 and 5 up to 1000

multiplesof3 = sum( [3*x for x in range(334)] )
multiplesof5 = sum( [5*x for x in range(200)] )
multiplesof15 = sum( [15*x for x in range(67)] )

result = multiplesof3 + multiplesof5 - multiplesof15

print(result)

#second solution by defining a function

def sumdivisibleby(n):
	lastone = target/n
	return sum( [n*x for x in range(int(lastone)+1)] )

target = 999
result2 = sumdivisibleby(3) + sumdivisibleby(5) - sumdivisibleby(15)
print(result2)