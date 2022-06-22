import array as arr

#create an array
numbers = arr.array('i',[2,3,4,8])
print(type(numbers))    #<class 'array.array'>

# using the typecode funtion to ccheck for the array's typecode
print(numbers.typecode)     #i - signed int

# length of the rray
print(len(numbers))         # Output: 4

# changing first element  
numbers[0] = 0     
print(numbers)    # Output: array('i', [0, 3, 4, 8]) 
   
# changing 3rd to 5th element  
numbers[2:5] = arr.array('i', [4, 6, 8])    
print(numbers)    # array('i', [0, 3, 4, 6, 8]) 

# delete items from array
del numbers[2]       # removing third element  
print(numbers)       # Output: array('i', [0, 3, 6, 8]) 

# concatenation
a=arr.array('d',[1.1 , 2.1 ,3.1,2.6,7.8])  
b=arr.array('d',[3.7,8.6])  
c=arr.array('d')  
c=a+b  
print("Array c = ",c)   # Output: Array c =  array('d', [1.1, 2.1, 3.1, 2.6, 7.8, 3.7, 8.6])
