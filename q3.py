def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if key in dct:              #Checking if key already exists in dct
        print(dct[key])         #Print original value
        dct[key] = value
    else:                       #Else if key does not exist, update dct with new key-value pair
        dct[key] = value
    return dct

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26
print(update_dictionary({}, "name", "Alice"))
print(update_dictionary({"age": 25}, "age", 26))