# Reverse a given list using a while loop.


numbers = [14, 62, 23, 34, 15]
reversed_list = []

index = len(numbers) - 1  # 4

while index >= 0:
    reversed_list.append(numbers[index])
    index = index - 1

print(reversed_list)