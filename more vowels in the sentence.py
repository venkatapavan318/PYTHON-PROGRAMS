'''wap to diaplay more vowels in the sentence '''

s = input("Enter a string: ")
words = s.split()
def count_vowels(word):
    return sum(1 for char in word if char.lower() in "aeiou")
vowels = max(words, key=count_vowels)
print("more vowels in the sentence :", vowels)
