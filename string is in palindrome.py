''' string in palindrome '''

s=input("enter a string : ")
rev=s[::-1]
print(rev)
if s==(rev):
    print('it is palindrome')
else:
    print('it is not a palindrome')
