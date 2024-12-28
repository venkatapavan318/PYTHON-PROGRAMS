''' program to input n value
display reverse of that number '''

n=int(input("enter  n value = "))
rev=0
t=n
while t>0:
    r=t%10
    rev=rev*10+r
    t=int(t/10)
print("reverse of ",n,"is" ,rev )
