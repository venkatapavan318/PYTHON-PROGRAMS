''' string and display its acronym or short form of the sentence '''

string = input("Enter a string: ")
short_form = ''.join(word[0].upper() for word in string.split())
print("short form:", short_form)
