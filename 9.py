#Python function to return next prime number 
def nextPrime(n):
    while True:
        n+=1
        for i in range(2,n):
            if n%i==0:
                break
            else:
                return 0