''' collection of characters '''

from collections import Counter
s = input("Enter a string: ")
freq = Counter(s)
for char, count in freq.items():
    print(f"{char} - {count}","times")




