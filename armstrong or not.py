''' program to input n value
    check whether a given number is armstrong number or not '''

n=int(input("Enter n value: "))
s=0
t=n
while t>0:
    r=t%10
    s=s+r**3
    t=int(t/10)
if n==s:
    print(n,"is an armstrong number")
else:
    print(n, "is not an armstrong number")
