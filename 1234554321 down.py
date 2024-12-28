rows = 5

for i in range(rows, 0, -1):
    line = ''
    for j in range(1, i + 1):
        line += str(j)
    line += ' ' * (2 * (rows - i))
    for j in range(i, 0, -1):
        line += str(j)
    print(line)
