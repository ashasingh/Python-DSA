# This is the CircularQueue class
class CircularQueue:
  
  # constructor to initiate queue with the max size
  def __init__(self, maxSize):
    self.queue = list()
    # user input value for maxSize
    self.maxSize = maxSize
    self.head = 0
    self.tail = 0

  # add element to the queue
  def enqueue(self, data):
    # if queue is full
    if self.size() == (self.maxSize - 1):
      return("Queue is full!")
    else:
      # add element to the queue
      self.queue.append(data)
      # increment the tail pointer
      self.tail = (self.tail+1) % self.maxSize
      return True
  
  # remove element from the queue
  def dequeue(self):
    # if queue is empty
    if self.size() == 0:
      return("Queue is empty!")
    else:
      # fetch data
      data = self.queue[self.head]
      # increment head
      self.head = (self.head+1) % self.maxSize
      return data
  
  # find the size of the queue
  def size(self):
    if self.tail >= self.head:
      qSize = self.tail - self.head
    else:
      qSize = self.maxSize - (self.head - self.tail)

    return qSize

# craete a queue with size 7
q = CircularQueue(int(7))

# add the elements
print(q.enqueue(10))
print(q.enqueue(20))
print(q.enqueue(30))
print(q.enqueue(40))
print(q.enqueue(50))
print(q.enqueue(70))
print(q.enqueue(80))    # error as queue is full

print(q.queue)

# remove elements from queue
print(q.dequeue())
print(q.dequeue())

# print queue
print(q.queue)
print(q.enqueue(10))

# print queue
print(q.queue)

# reove elements from queue
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
