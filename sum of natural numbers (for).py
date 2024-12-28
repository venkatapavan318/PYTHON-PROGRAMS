''' program to input n value
    display the sum of n natural numbers  '''

n=int(input("Enter n value : "))
s=0
for i in range (1,n+1):
    s=s+i
    print(i)
print("sum is ...." ,s )
