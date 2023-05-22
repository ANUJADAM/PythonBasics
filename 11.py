# Single line function to calculate factorial of a number in python
n = int(input("enter a number :"))
f = lambda n: n*f(n-1) if n>0 else 1
print("Factorial of given number is",f(n))
