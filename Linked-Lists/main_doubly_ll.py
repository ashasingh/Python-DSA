class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

class doubly_linked_list:
    def __init__(self):
      self.head = None

    # Adding data elements		
    def addElements(self, NewVal):
      NewNode = Node(NewVal)
      NewNode.next = self.head
      if self.head is not None:
         self.head.prev = NewNode
      self.head = NewNode

    # Print the Doubly Linked list		
    def listprint(self, node):
      while (node is not None):
         print(node.data),
         last = node
         node = node.next

    # method to insert the element at specific position
    def insertIn(self, prev_node, NewVal):
      if prev_node is None:
         return
      NewNode = Node(NewVal)
      NewNode.next = prev_node.next
      prev_node.next = NewNode
      NewNode.prev = prev_node
      if NewNode.next is not None:
         NewNode.next.prev = NewNode

    # method to insert element at the end
    def insertAtEnd(self, NewVal):
      NewNode = Node(NewVal)
      NewNode.next = None
      if self.head is None:
         NewNode.prev = None
         self.head = NewNode
         return
      last = self.head
      while (last.next is not None):
         last = last.next
      last.next = NewNode
      NewNode.prev = last
      return

# create a doubly Linked List
dllist = doubly_linked_list()
dllist.addElements(12)
dllist.addElements(8)
dllist.addElements(62)
dllist.listprint(dllist.head)

# Inserting into Doubly Linked List

# insert at a given position
dllist.insertIn(dllist.head.next, 13)
dllist.listprint(dllist.head)

# insert at the end
dllist.insertAtEnd(45)
dllist.listprint(dllist.head)
