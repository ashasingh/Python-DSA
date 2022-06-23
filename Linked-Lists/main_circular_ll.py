class Node:
   def __init__(self, data):
      self.data = data
      self.next = None

class circularLinkedList:  
   def __init__(self):
      self.root = None
    
    # method to add new elements to the list  
   def add(self, data):
      new_node = Node(data)
      temp = self.root    
      new_node.next = self.root

      if self.root is not None:
         while(temp.next != self.root):
            temp = temp.next
         temp.next = new_node
      else:
         new_node.next = new_node
      self.root = new_node

    # method to print circular LL
   def listCLL(self):
      temp = self.root
      if self.root is not None:
         while(True):
            print(temp.data)
            temp = temp.next
            if (temp == self.root):
               break
           
           
# create and add elements to CLL
my_list = circularLinkedList()
my_list.add(56)
my_list.add(78)
my_list.add(12)

# print the CLL
print("The data is : ")
my_list.listCLL()
