# Write a program that calculates the sum of all the numbers from 1 to n
# and prints the result which are odd numbers


### for(int i=0;i<=n;i++)  ----> for i in range(n)
# while(n>100) --> while n > 100:

# }

n = int(input())

sum = 0
for i in range(1, n):
    if i % 2 ==0:
        sum += i


print("Kjo eshte shuma" + str(sum))