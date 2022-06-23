class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SinglyLinkedList:
    def __init__(self):
      self.root = None
    
    # method to traverse through the linked list
    def listprint(self):
      printval = self.root
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval
    
    # method to insert new node at begining
    def insertAtBegining(self,newdata):
      NewNode = Node(newdata)
      NewNode.nextval = self.root
      self.root = NewNode
      
    # method to insert new node at end
    def insertAtEnd(self, newdata):
      NewNode = Node(newdata)
      if self.root is None:
         self.root = NewNode
         return
      last = self.root
      while(last.nextval):
         last = last.nextval
      last.nextval=NewNode

    # method to insert new node in between 2 nodes
    def insertInbetween(self,middle_node,newdata):
      if middle_node is None:
         print("The mentioned node is absent")
         return
      NewNode = Node(newdata)
      NewNode.nextval = middle_node.nextval
      middle_node.nextval = NewNode

    # method to remove node
    def removeNode(self, Removekey):
      HeadVal = self.root
         
      if (HeadVal is not None):
         if (HeadVal.dataval == Removekey):
            self.root = HeadVal.nextval
            HeadVal = None
            return
      while (HeadVal is not None):
         if HeadVal.dataval == Removekey:
            break
         prev = HeadVal
         HeadVal = HeadVal.nextval
      if (HeadVal == None):
         return
      prev.nextval = HeadVal.nextval
      HeadVal = None
      

# creation of singly linked list
list1 = SinglyLinkedList()
list1.root = Node("January")
e2 = Node("February")
e3 = Node("March")

# Link first Node to second node
list1.root.nextval = e2

# Link second Node to third node
e2.nextval = e3

# traversing through singly linked list
list1.listprint()

# Insertion in a Linked List

# at the begining
list1.insertAtBegining("December")
list1.listprint()

# Inserting at the End
list1.insertAtEnd("April")
list1.listprint()

# Inserting in between two Data Nodes
list1.insertInbetween(list1.root.nextval,"May")
list1.listprint()

# Removing an Item
list1.removeNode("May")
list1.listprint()
