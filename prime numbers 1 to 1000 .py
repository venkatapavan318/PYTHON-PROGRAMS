''' program to input start and end value check whether a given numbers 1 to 1000 prime numbers '''

s=int(input("enter a start value = "))
e =int(input("enter a end value = "))
while s<=e:
    i=2
    while i<s:
        if s%i==0:
            break
        i=i+1
    if i==s:
        print (s,' is prime numbers ' )
    s=s+1
    
