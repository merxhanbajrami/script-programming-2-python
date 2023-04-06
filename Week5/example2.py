# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
from math import fsum

numbers = [i for i in range(1, 11)]
print(numbers)

sum = 0

for num in numbers:
    if num % 2 == 0:
        sum = sum + num

print("Shuma eshte kjo " + str(sum))

suma_list_comp = fsum([num for num in numbers if num % 2 == 0])

print("Shuma me list comprehension" + str(suma_list_comp))
