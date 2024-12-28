''' Write a program to display following format of diamond '''

r = int(input('enter a number of rows: '))
for i in range(1, r + 1):
    for j in range(1, r - i + 1):
        print(" ", end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("1", end="")
        else:
            print(" ", end="")
    print()
for i in range(r - 1, 0, -1):
    for j in range(1, r - i + 1):
        print(" ", end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("1", end="")
        else:
            print(" ", end="")
    print()
