#  Write a python script to reverse a tuple
t=eval(input("Enter numbers separated by comma"))
print("User entered tuple is",t)
l=list(t)
l.reverse()
t=tuple(l)
print("Reverse of tuple is",t)