r=lambda x, y:x if x > y else y
n1 = int(input("enter a 1st value : "))
n2 = int(input("enter a 2nd value : "))
biggest = r(n1,n2)
print(f"biggest number is ...{biggest}")
