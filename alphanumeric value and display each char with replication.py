'''alphanumeric value and display each char with replication'''

str1 = input("Enter a string: ")
str2 = ""
count = 1
for i in range(len(str1)):
    if str1[i].isdigit():
        count = int(str1[i])
    else:
        str2 += str1[i] * count
print("Result:", str2)
