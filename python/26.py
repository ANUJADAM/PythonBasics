# Pyhton script to check prime number
n = int(input("Enter a number :"))
if n<2:
    print(n,"is not a prime number")
else:
   for i in range(2,n):
       if n%i==0:
           print(n,"is not a prime number")
           break
   else:
       print(n,"is a prime number")
        