''' program to input start and end value check whether a given number is prime or not '''

n=int(input("enter a n value = "))
i=2
while i<n:
    if n%i==0:
        print(n,"is not a prime number")
        break
    i=i+1
    if i==n:
        print(n,"is a prime number")
        
