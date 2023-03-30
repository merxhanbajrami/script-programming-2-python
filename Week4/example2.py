fruits = ["apple", "banana", "cherry"]

print(fruits)

fruits[0] = "grape"
# fruits[1] = 60
print(fruits)

# concatenation
mixed_list = fruits + [1, 2, 3] + ["strawberry"]
print(mixed_list)

# repeating
doubled_list = fruits * 2
print(doubled_list)  # Output: ['grape', 'banana', 'cherry', 'grape', 'banana', 'cherry']

numbers_list = [0, 1, 2, 3, 4, 5, 6]
new_list = numbers_list * 3

#product
my_list = [el*3 for el in numbers_list] #-> list comprehension

print(my_list)

