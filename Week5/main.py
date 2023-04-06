# eshte e dhene nje list, te krijohet nje liste tjeter e cila permban katroret e numrave ne listen e dhene, duke perdorur list comprehension


numbers = [1, 2, 3, 4, 5]

squares = []

for element in numbers:
    squares.append(element*element)


print(numbers)
print(squares)


squares_list_comprehension = [el*el for el in numbers]

print(squares_list_comprehension)
