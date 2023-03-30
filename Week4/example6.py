###list fruits that have letter a inside
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for fruit in fruits:
  if "a" in fruit:
    newlist.append(fruit)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [fruit for fruit in fruits if "a" in fruit]

print(newlist)