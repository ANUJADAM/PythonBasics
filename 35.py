# recursive function to calculate sum of frist N natural numbers
def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

# change this value for a different result
num = int(input("Enter a number:"))

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))