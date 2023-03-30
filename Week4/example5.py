###
# list me elementet 0,9
# without comprehension
my_list = []
for i in range(10):
    my_list.append(i)

print(my_list)

# list comprehension
new_list = [i for i in range(10)]
print(new_list)

my_list1 = []
for i in range(10):
    if i % 2 == 0:
        my_list1.append(i*2)
    else:
        my_list1.append(i*3)


print(my_list1)

# list comprehension
new_list1 = [i for i in range(10) if i % 2 == 0]
print(new_list1)
