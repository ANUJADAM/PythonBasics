# python script to count the frequency of the elements of tuple
t=(1,2,3,4,2,1,3,2,1,1,1)
i=0
for e in t:
    if t.index(e) == i:
        print(e,"---",t.count(e))
    i+=1