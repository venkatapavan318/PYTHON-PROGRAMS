def count_frequency(my_list):
    freq = {}
    for item in my_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq
my_list = [1, 2, 3, 2, 2, 1, 3, 4, 5, 4, 5, 5]
frequency = count_frequency(my_list)
for key, value in frequency.items():
    print(f"Element {key} occurs {value} times in the list.")
