''' program to input n  value
    check whether a given number 1 to 1000 between armstrong  numbers '''

n = 1
while n <= 1000:
    s = 0
    t = n
    while t > 0:
        r = t % 10
        s = s + r ** 3
        t = int(t / 10)
    if n == s:
        print(n, "is an armstrong numbers ")
    n = n + 1
