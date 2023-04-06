# Use a list comprehension to generate a list of prime numbers between 2 and a given number N.

print("Fusni vleren e n:")
# n = int(input())

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
##prime numbers: 1,3,5,7,11,13 ---> kan vetem dy pjestues # me 1 dhe veten
##numrat tek
#tek = [x for x in range(2, 16) if x % 2 != 0]
#print(tek)

###numrat e thjeshte me list comprehension
thjesht = [el for el in range(2, 16) if all(el % y != 0 for y in range(2, int(el ** 0.5) + 1))]
print(thjesht)

### menyra e pare
# for el in numbers:
# el e kena numrin
#    pjesetues = 0

#    for i in range(1, el + 1):
#        if el % i == 0:
#            pjesetues = pjesetues + 1

#    if pjesetues <= 2:
#        print("Numri eshte prime" + str(el))

###menyra e dyte with flag logic
# for el in numbers:
#    # el e kena numrin
#    pjesetohet = False
#    for i in range(2, int(el/2) + 1):
#        if el % i == 0:
#            pjesetohet = True
#
#    if pjesetohet == False:
#        print("Numri eshte prime" + str(el))

###menyra e dyte with flag logic
# for el in numbers:
#    # el e kena numrin
#    pjesetohet = False
#    for i in range(2, int(el**0.5) + 1):
#        if el % i == 0:
#            pjesetohet = True
#
#    if pjesetohet == False:
#        print("Numri eshte prime" + str(el))


# te shkoni deri ne el-1, kontrollo sa pjesetues i ka , 9->2,3,4,5,6,7,8
# te shkoni deri ne el/2, kontrollo sa pjeseues i ka -> 2,3,4,5
# te shkoni deri ne square_root(), kontrollo sa pjesetues i ka -> 2,3
