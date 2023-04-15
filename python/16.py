# Recursive function to calculate the sum of squres of frist N natural numbers 
# n = int(input("Enter a number"))
# def sum(n):
#     if n==1:
#         return 1
#     return n**2+sum(n-1)
# print("Sum of squres is",sum(n))

n = int(input("Enter a number"))
sum = lambda n : 1 if n == 1 else n**2 + sum(n-1)
print("Sum of squres is",sum(n))

