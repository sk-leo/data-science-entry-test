def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    for x in range(len(lst)):                   #Using for loop to go through the list
                                                #Log: originally used 'for x in lst' which resulted in "List indices must be int not str" error as x is a value not the index. Changed to 'range(len(lst))' to iterate by index instead.
        if lst[x] == find_val:                  #if current item in list matches find_val
            lst[x] = replace_val                #replaces current item with replace_val
    return lst


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"
print(find_and_replace([1,2,3,4,2,2], 2, 5))
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))