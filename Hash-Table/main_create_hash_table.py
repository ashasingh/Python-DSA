# create a hash table of 10 indexes
hashTable = [[],] * 10

# create a hash function using division method
def hashFunction(key):
    return(key%10)


#insert data 
def insertData(key, data):
    index = hashFunction(key)
    hashTable[index]= [key, data]

def insertDataColl(key, data):
    index = hashFunction(key)
    hashTable[index].append([key, data])
    
def removeData(key):
    index = hashFunction(key)
    hashTable[index] = []

insertData(123, "apple")
insertData(432, "mango")
insertData(213, "banana")   # this will override the apple dataset as both keys have same hash function
insertData(654, "guava")

print(hashTable)

removeData(123)
print(hashTable)

# lets make use of collision resolution by chaining
insertDataColl(123, "apple")
insertDataColl(213, "banana")
print(hashTable)
