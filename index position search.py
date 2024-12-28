def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return "Element not found"

if __name__ == '__main__':
    elements = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    search_element = int(input("Enter element to search: "))
    result = linear_search(elements, search_element)
    print(result)
