def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if type(x) == int and type(y) == int:           #Checking if both x and y are numeric
        x, y = y, x                                 #Swap x and y
        print("x:", x, "y:", y)
    else:
        print("Both x and y must be numeric.")
        return -1

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
swap("Apple",10)
swap(9,17)
