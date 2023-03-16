### Write a program that asks the user for two dates
# (in the format YYYY-MM-DD) and determines which date comes first.

data1 = str(input()) ## 2023-03-16
data2 = str(input()) ## 2023-03-15 ->kjo vjen e para

print(data2[-2:])


if int(data1[:3]) > int(data2[:3]):
    print("Kjo eshte me perpara" + str(data2))
elif int(data1[:3]) < int(data2[:3]):
    print("Kjo eshte me perpara" + str(data1))
else:
    ###te dy vitet jane te barabarte
    if int(data1[5:7]) > int(data2[5:7]):
        print("Kjo eshte me perpara" + str(data2))
    elif int(data1[5:7]) < int(data2[5:7]):
        print("Kjo eshte me perpara" + str(data1))
    else:
        ###te dy muajt e barabarte
        if int(data1[-2:]) > int(data2[-2:]):
            print("Kjo eshte me perpara" + str(data2))
        elif int(data1[-2:]) < int(data2[-2:]):
            print("Kjo eshte me perpara" + str(data1))
        else:
            ###te dyjat te barabarta
            print("Datat jane te barabarta!")