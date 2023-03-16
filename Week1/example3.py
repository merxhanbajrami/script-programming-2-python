##Write a Python program that asks the user to enter their age, and then prints out a message that says "
# You are [age] years old. In 10 years, you will be [age + 10] years old."

print("Fut moshen tuaj:")
age = int(input())
age_ten = age + 10

print("You are {age} years old. In 10 years, you will be {age_ten} years old".format(age=age, age_ten=age_ten))
print(f"You are{age} years old. In 10 years, you will be {age + 10} years old")