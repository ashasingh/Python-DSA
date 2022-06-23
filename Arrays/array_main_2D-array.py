from array import *

# create 2d array
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

print(T[0])         # Output: [11, 12, 5, 2]
print(T[1][2])      # Output: 10

# traverse through the array
for col in T:
   for row in col:
      print(row,end = " ")
   print()
   
# inserting values to the array
T.insert(2, [0,5,11,13,6])
print(T)        # Output: [[11, 12, 5, 2], [15, 6, 10], [0, 5, 11, 13, 6], [10, 8, 12, 5], [12, 15, 8, 6]]

# Updating values
T[2] = [11,9]
T[0][3] = 7
print(T)        # Output: [[11, 12, 5, 7], [15, 6, 10], [11, 9], [10, 8, 12, 5], [12, 15, 8, 6]]

# Deleting values
del T[3]
print(T)        # Output: [[11, 12, 5, 7], [15, 6, 10], [11, 9], [12, 15, 8, 6]]
