# write recursive function to print frist N natural numbers in reverse
def printEvenreverse(n):
    if n>0:
        print(2*n,end=" ")
        printEvenreverse(n-1)
printEvenreverse(int(input("Enter a number:")))