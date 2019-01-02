print(" ") 
print(" ")
ID=input("enter your ID: ")
ID_12=[1,2,1,2,1,2,1,2,1]
ID_mul=[0,0,0,0,0,0,0,0,0]
ID_sum=[0,0,0,0,0,0,0,0,0]
while 1:   
    if len(ID)==9:
        print("Your ID is: ",end="")
        for i in ID:
            print(i," , ",end="")
        print()

        print("the 1,2,1 : ",end="")
        for i in ID_12:
            print(i," , ",end="")
        print()

        print("the multip: ",end="")
        for i in range (0,9):
            ID_mul[i]=int(ID[i])*ID_12[i]
            if ID_mul[i]>9:
                print(ID_mul[i],", ",end="")
            else:
                print(ID_mul[i]," , ",end="")
        print()

        print("the MulSum: ",end="")
        for i in range (0,9):
            if ID_mul[i]>9:
                ID_sum[i]=ID_mul[i]%10+int(ID_mul[i]/10)
                print(ID_sum[i]," , ",end="")
            else:
                ID_sum[i]=ID_mul[i]
                print(ID_sum[i]," , ",end="")
        print()
        
        SumAll=0
        for i in range(0,9): 
            SumAll=SumAll+ID_sum[i]
        print("the sum of all the numbers is: ",SumAll)
        if SumAll%10==0:
            print("your ID is CORRECT!")
            break
        else:
            ID=input("your ID is uncorrect, please try again: ")
    else:
        ID=input("you need 9 digits. Try again: ")

   