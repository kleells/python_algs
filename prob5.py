# Write a function that takes in a list of numbers
# and returns the product of the numbers in the list.

def multiple_list(list) :
    result = 1
    for number in list:
         result = result * number
    return result


list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiple_list(list1))
print(multiple_list(list2))