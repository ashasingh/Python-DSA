class Stack:
    def __init__(self):
      self.stack = []

    # push element to the top
    def push(self, dataval):
      if dataval not in self.stack:
         self.stack.append(dataval)
         return True
      else:
         return False
        
    # remove element from the top
    def pop(self):
      if len(self.stack) <= 0:
         return ("No element in the Stack")
      else:
         return self.stack.pop()
    # to peek the top element of stack
    def peek(self):     
        return self.stack[-1]
    
    

# create stack 
AStack = Stack()

# add elements to the stack
AStack.push("Mon")
AStack.push("Tue")
AStack.push("Wed")
AStack.push("Thu")

# print stack
print(AStack.stack)         # Output: ['Mon', 'Tue', 'Wed', 'Thu']

# remove elements from stack
print(AStack.pop())         # Output: Thu
print(AStack.pop())         # Output: Wed

# print stack
print(AStack.stack)         # Output: ['Mon', 'Tue']

# peek the element at the top of stack
print(AStack.peek())        # Output: Tue

