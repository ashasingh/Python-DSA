
list1 = [1,3,5,2,4,6]

print(list1)    # Output: [1, 3, 5, 2, 4, 6]

# print length of list
print(len(list1))   # Output: 6

# access item through indexing
print(list1[0])     # Output: 1
print(list1[-1])     # Output: 6

# access item through slicing
print(list1[1:])    # Output: [3, 5, 2, 4, 6]
print(list1[3:5])    # Output: [2, 4]

# traversal through a list
for x in list1:
    print(x)

# traversal through list using indexing
for i in range(len(list1)):
    print(list1[i])
    
# Insertion in the list

# to the end
list1.append(12)
print(list1)        # Output: [1, 3, 5, 2, 4, 6, 12]

# add more element at once
list1.extend([9,1,4])
print(list1)        # Output: [1, 3, 5, 2, 4, 6, 12, 9, 1, 4]

# insertion at a particular index
list1.insert(1,345)
print(list1)        # Output: [1, 345, 3, 5, 2, 4, 6, 12, 9, 1, 4]

# Deletion in the list

# to the end
list1.pop()
print(list1)        # Output: [1, 345, 3, 5, 2, 4, 6, 12, 9, 1]

# remove an element at a particular index
list1.pop(1)
print(list1)        # Output: [1, 3, 5, 2, 4, 6, 12, 9, 1]

# remove a particular item - only removes the 1st occurance
list1.remove(1)
print(list1)        # Output: [3, 5, 2, 4, 6, 12, 9, 1]


# Search an item in the list
# multiple ways to do that; 

# linear search; find '1'
for x in list1:         # Output: Found at index:  7
    if x == 1 :
        print("Found at index: ", list1.index(x)) 

# Update an element in list

# using indexing
list1[1] = 1
print(list1)        # Output: [3, 1, 2, 4, 6, 12, 9, 1]


# In-built functions

# copy a list
list2 = list1.copy()
print(list2)        # Output: [3, 1, 2, 4, 6, 12, 9, 1]

# clear elements of a list
list2.clear()
print(list2)        # Output: []

# count occurance of a particular item
print(list1.count(1))   # Output: 2

# reverse a list
list1.reverse()
print(list1)            # Output: [1, 9, 12, 6, 4, 2, 1, 3]

# sort a list
list1.sort()
print(list1)            # Output: [1, 1, 2, 3, 4, 6, 9, 12]



