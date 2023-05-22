# python script to arrange three words in dictionary order
print = ("Enter three city name")
a,b,c = input(),input(),input()
if a<b<c:
    print(a,b,c)
elif a<c<b:
    print(a,c,b)
elif b<a<c:
    print(b,a,c)
elif b<c<a:
    print(b,c,a)
elif c<a<b:
    print(c,a,b)
else :
    print(c,b,a)




# second method
# print = ("Enter three city name")
# a,b,c = input(),input(),input()
# x = min(a,b,c)
# print(x) 
# if x==a:
#     print(min(b,c),max(b,c))
# elif x==b:
#     print(min(a,c),max(a,c))
# else:
#     print(min(a,b),max(a,b))




# third method
#  for x in sorted(input("Enter comma seperated three city name").split(',')) if print(x,end=' ')




