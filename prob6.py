# Write an algorithm that prints the non-repeating
# integers in a list.

def nonrepeating(list):

    # insert elements of list into dictionary (hash table)
    elements = {}
    for i in range(len(list)):
        if list[i] not in elements:
            elements[list[i]]=0
        elements[list[i]]+=1
    
    # traverse through elements in dictionary
    for j in elements:
        if (elements[j] == 1):
            print(j)

list = [1, 5, 1, 6, 8, 5, 7, 9, 9]
nonrepeating(list)