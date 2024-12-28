'''reverse every word of a string '''

def reverse_words(string):
    words = string.split()
    reversed_words = [word[::-1] for word in words]
    reversed_string = ' '.join(reversed_words)
    return reversed_string
strings =["durgasoft software solution","durgasoft","software","solution"]
for string in strings:
    result = reverse_words(string)
    print(result)
