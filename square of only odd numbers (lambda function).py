n=int(input("enter a n value : "))
result=list(map(lambda x:x**2, filter(lambda x:x%2!=0, range(1,n+1))))
print(f"square of only odd numbers from 1 to {n}...: {result}")
