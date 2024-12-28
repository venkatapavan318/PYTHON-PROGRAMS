'''word which has more number of characters'''

s = input("Enter a string: ")
longest_word = max(s.split(), key=len)
print("longest word is :", longest_word)
