''' string with alpha numeric value '''


s = input("Enter a string with alphanumeric values: ")
alphabets = ""
digits = ""
for char in s:
    if char.isalpha():
        alphabets += char
    elif char.isdigit():
        digits += char
print("Alphabets:", alphabets)
print("Digits:", digits)
