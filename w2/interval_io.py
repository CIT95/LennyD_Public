#inputing a starting number
while True:
    Number1 = int(input("Enter a number: "))

#inputting an ending number to input    
    Number2 = int(input("Now enter another number: "))

#Verifying the starting input is less that in the ending
    if int(Number1) > int(Number2):
        print ('Invalid entry. Your starting value needs to be less than your ending value.')
        print ('Try again')
#Ascending order
    else:
        for i in range(int(Number1),int(Number2)+1):
            print(i) 
