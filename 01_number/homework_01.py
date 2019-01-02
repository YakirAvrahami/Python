num = int (input ("Enter number: "))
if num>=0 and num<10:
    if num == 0:        print("zero")
    elif num == 1:      print("one")
    elif num == 2:      print("two")
    elif num == 3:      print("three")
    elif num == 4:      print("four")
    elif num == 5:      print("five")
    elif num == 6:      print("six")
    elif num == 7:      print("seven")
    elif num == 8:      print("eight")
    else:               print("nine")
elif num>9 and num <100:
    units = num % 10
    tens = int ( num / 10 )
    print(tens, " + " ,units, " = " ,units+tens)
elif num>99 and num<1000:
    units = num % 10
    tens = int ( (num/10)%10 )
    hundreds = int ( num / 100 )
    print(hundreds," * ",tens," * ",units," = ",units*tens*hundreds)
else:
    print("your number has more than 3 digits!")
