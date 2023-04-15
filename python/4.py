# python script to remove duplicates from a list of basestring
names=[]
n=int(input("How many names you want to enter"))
for i in range(n) :
    print(i+1,"Enter names")
    names.append(input())
s=set(names)
names=list(s)
for x in names:
    print(x)
