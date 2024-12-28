''' program to input start and end value check whether a given number is prime end with 3'''

s=int(input("enter a start value = "))
e =int(input("enter a end value = "))
while s<=e:
    i=2
    while i<s:
        if s%i==0:
            break
        i=i+1
    if i==s and s%10==3:
        print (s,' is prime number ' )
    s=s+1
    
