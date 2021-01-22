#Comparing two Integers in Python.  
#Get user input 
Number1 = int(input("Enter a number: "))
Number2 = int(input("Now enter another number: "))
if Number1 > Number2:
    print("The ending of number cannot be greater than the starting number.")
    print ('Try again')
#Range of Value
for val in range(Number1, Number2 + 1):
   if val > 1:
      for i in range(2, val):
         if (val % i) == 0:
            break
      else:
         print(val)



#https://www.youtube.com/results?search_query=how+to+determine+if+a+number+is+prime
#https://scanftree.com/programs/python/python-program-to-print-all-prime-numbers-in-an-interval/

