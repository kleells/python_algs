# Write a recursive function that takes in a number and
# returns the sum of the numbers from 0 to the number.

def rec_func(num):
    # base case
    if num == 1:
        return 1
    else: product = num * rec_func(num - 1)
    return product

print(rec_func(5))