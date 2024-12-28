def print_pattern(n):
    for i in range(n, 0, -1):
        row = ""
        for j in range(1, i + 1):
            row += str(j)
        for k in range(0, 2*(n-i)):
            row += " "
        for j in range(i, 0, -1):
            row += str(j)
        print(row)

    for i in range(2, n + 1):
        row = ""
        for j in range(1, i + 1):
            row += str(j)
        for k in range(0, 2*(n-i)):
            row += " "
        for j in range(i, 0, -1):
            row += str(j)
        print(row)

print_pattern(5)
