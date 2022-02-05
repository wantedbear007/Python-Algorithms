print('Binary Search')

# Binary Search: Searching for an item in a list.
# With loop

# ITERATIVE BINARY SEARCH

data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19]


def iterative_binary_search(list_data, target):
    low = 0
    high = len(list_data)

    while low <= high:
        middle_index = (high + low) // 2
        if target == list_data[middle_index]:
            return True
        elif target < list_data[middle_index]:
            high = middle_index - 1
        else:
            low = middle_index + 1
    return False


# print(iterative_binary_search(data, 16))

# WITHOUT LOOP
# RECURSIVE BINARY SEARCH

def recursive_binary_search(list_data, target, high, low):
    if low > high:
        return False
    else:
        middle_value = (high + low) // 2
        if list_data[middle_value] == target:
            return True
        elif target < list_data[middle_value]:
            return recursive_binary_search(list_data, target, middle_value - 1, low)
        else:
            return recursive_binary_search(list_data, target, high, middle_value + 1)


print(recursive_binary_search(data, 16, len(data), 0))
