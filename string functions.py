'''string function '''

s=input('enter any string : ')
if s.isalpha():
    print("alphabets")
    if s.isalnum():
        print("alphanumeric")
    if s.islower():
        print("string is lower case")
    else:
        if s.upper():
            print("string is upper case")
else:
    if s.isdigit():
        print("this is digit")
    else:
        if s.isspace():
            print("spaces")
        else:
            print("special characters")
        
