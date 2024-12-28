''' progarm to input n value
     display the mathematical table of that number '''

n=int(input("Enter n value : "))
for i in range (1,11):
    print(" %d * %d = %d "%(n,i,(n*i)))
    print(n, '*' ,i, '=', n*i)
