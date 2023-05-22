# recursive function to print  frist N even natural numbers
def Neven(n):
    if n>0:
        Neven(n-1)
        print(2*n)
n=int(input("Enter a number:"))
Neven(n)

        