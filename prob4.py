# Write a recursive function that takes in a list
# of strings and returns the words capitalized.

def all_caps(lst):
    if len(lst) == 0:
        return ""
    else:       
        return (f"{lst[0].upper()} {all_caps(lst[1:])}")

test_list = ['apple', 'banana', 'orange', 'grape', 'kiwi']
print(all_caps(test_list))