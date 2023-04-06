# Given a list of numbers, use a list comprehension to find the product of all the numbers in the list
from functools import reduce
import operator

numbers = [1, 2, 3, 4, 5]  # ->120
product = 1
for el in numbers:
    product = product * el

print("Prodhimi eshte" + str(product))

####more advanced way

pr = reduce(operator.mul, numbers)
print(pr)
