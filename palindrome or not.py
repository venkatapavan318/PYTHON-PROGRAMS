''' program to input n value
    display reverse of the number is palindrome or not '''

n=int(input("enter n value = "))
rev=0
t=n
while t>0:
    r=t%10
    rev=rev*10+r
    t=int(t/10)
if n==rev:
    print(n, "is a palindrome number")
else:
    print(n, " is not a palindrome number")
    
