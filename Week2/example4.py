# Problem2: Write a program that asks the user for three numbers and
# checks if they form a Pythagorean triple (i.e. a^2 + b^2 = c^2).


###tre vlera a-> kateta e pare, b -> kateta e dyte dhe c->hipotenuza
import math as m

a = int(input())
b = int(input())
c = int(input())

sq_a = m.pow(a, 2)
sq_b = m.pow(b, 2)
sq_c = m.pow(c, 2)

if sq_a + sq_b == sq_c:
    print("plotesojn kushtin e teoremes se pitagores!")
else:
    print("nuk e plotesojn kushtin e teoremes se pitagores!")
