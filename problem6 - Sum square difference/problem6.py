import numpy as np

target = 100

my_array = np.array(range(1,101))

sum_square_difference = sum(my_array)**2 - my_array.dot(my_array)

print(sum_square_difference)