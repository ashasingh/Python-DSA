# Import queue from Queue Module
from queue import Queue

# Initializing a queue
q = Queue(maxsize = 5)  # its optional to give a maxsize

# print size of the queue
print(q.qsize())    # cureently queue is empty = 0

# Adding of element to queue
q.put('a')
q.put('b')
q.put('c')
q.put('d')
q.put('e')

# Return Boolean for Full
print("\nFull: ", q.full())     # as elements reached a max to 5

# print elements of the queue
print(q.queue)

# Removing element from queue
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())

# Return Boolean for Empty
print("\nEmpty: ", q.empty())       # true; as there are no elements

# add elements and print elements of the queue
q.put('a')
print(q.queue)

#checks to see i queue is full or empty
print("Empty: ", q.empty())
print("Full: ", q.full())
