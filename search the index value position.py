''' to search the index value position '''


def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
list = [12, 34, 56, 78, 90, 123, 456, 789]
search = int(input("Enter element to search: "))
result = linear_search(list,search)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
