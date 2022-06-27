# Max-Heap data structure in Python

# call max-heap heapify
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2 
    
    if l < n and arr[i] < arr[l]:
        largest = l
    
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest)

# add elemnt to tree at the end and call heapify
def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum);
        for i in range((size//2)-1, -1, -1):
            heapify(array, size, i)

# delete element and call heapify
def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break
        
    array[i], array[size-1] = array[size-1], array[i]

    array.remove(num)
    
    for i in range((len(array)//2)-1, -1, -1):
        heapify(array, len(array), i)

## create empty array  
arr = []

# Insertion in Max-Heap
insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)
print ("Max-Heap array: " + str(arr))

# delete item from array
deleteNode(arr, 4)
print("After deleting an element: " + str(arr))

# get the max element
print("Peek of maximum element: " + str(arr[0]))

# Extract max - get the max element from array and delete from the array
print("Extract Max: " + str(arr[0]))
deleteNode(arr, arr[0])
print ("Max-Heap array: " + str(arr))

