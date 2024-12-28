height = 7

for i in range(height):
    if i == 0 or i == height - 1:
        print('#' * height)
    else:
        spaces = ' ' * i
        print(spaces + '#')
