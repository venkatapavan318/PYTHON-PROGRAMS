''' program to input n value
    check whether the given number is strong or not '''

from math import factorial
n=int(input("Enter n value = "))
s=0
t=n
while t>0:
    r=t%10
    s=s+factorial(r)
    t=int(t/10)
if n==s:
    print(n,"is a strong number ")
else:
    print(n,"is not a strong number")
    
