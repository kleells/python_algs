# Write an algorithm that checks if a string contains another string.

    # If it does, return True; otherwise, return False.
    # Example: When checking if string "Hello world"
    # contains "Hello", the function should return
    # True. If checking if the same string contains "Bye",
    # the function should return False.

def nested_str(str, word):
    return (word in str)

string = "Hello world"
test_str = "Bye"

print(nested_str(string, test_str))