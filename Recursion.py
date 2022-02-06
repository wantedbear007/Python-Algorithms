print('Recursion')

# Finding uppercase letter in a string

# ITERATIVE METHOD

input_str_1 = 'Bhanupratap'
input_str_2 = 'BhanuPratap'
input_str_3 = 'bhanupratap'


def find_uppercase_iterative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]
        return 'No letter is uppercase.'


# print(find_uppercase_iterative(input_str_3))

def find_uppercase_recursive(input_str, idx=0):
    if input_str[idx].isupper():
        return input_str[idx]
    if idx == len(input_str) - 1:
        return 'No uppercase letters found.'
    return find_uppercase_recursive(input_str, idx + 1)


# print(find_uppercase_recursive(input_str_3))

# CALCULATING STRING LENGTH

str_value = 'bhanupratap'


def iterative_str_len(str_value):
    count = 0
    for i in str_value:
        count += 1
    return count


# print(iterative_str_len(str_value))

# def recursive_str_len(str_value, count=0):

# print(str_value)

# VOVEL COUNTER

str_value_1 = 'googlea'
str_value_2 = 'xyz'

vovels = 'aeiou'


def iterative_vovel(str_value):
    for i in vovels:
        for v in str_value:
            if v == i:
                return True
        return False


# print(iterative_vovel(str_value_2))
# print(iterative_vovel(str_value_1))

# def recursive_vovel(str_value):
#     if str_value == '':
#         return 0
#     if str_value[0].lower() not in vovels and str_value[0].isalpha():
#         return 1 + recursive_vovel(str_value[1:])
#     else:
#         return recursive_vovel(str_value[1:])

def recursive_vovels(str_value, count=0):
    if str_value == '':
        return False
    else:
        if str_value[count].lower() not in vovels:
            return recursive_vovels(str_value[1:])
        else:
            return True

#
# print(recursive_vovels(str_value_1))
# print(recursive_vovels('srj'))
