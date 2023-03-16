##flow control statements
x = 10
if x > 5:
    print(f"{x} is greater than 5")
    for i in range(5):
        if i == 3:
            continue
        print(i)