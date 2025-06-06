def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    return s[::-1]  #Using string slicing starting at the end of the string, and moving backwards by 1 (-1)

# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
print(string_reverse("Hello World"))
print(string_reverse("Python"))