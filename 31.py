# Print frist N even numbers in reverse order
n = int(input("Enter a number:"))
for i in range(2*n,1,-2):
    print(i,end=' ')