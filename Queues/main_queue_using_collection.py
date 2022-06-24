# Import module
from collections import deque

# Initializing a queue
q = deque()

# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')
q.append('d')

# print queue
print(q)

# Removing elements from begining
print(q.popleft())
print(q.popleft())
print(q.popleft())

# print queue after deletion
print(q)

