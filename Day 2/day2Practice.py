'''class Node:
   def _init_(self, dataval=None):
      self.dataval = dataval
      self.nextval = None
class SLinkedList:
   def _init_(self):
      self.headval = None
   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval
list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list.headval.nextval = e2
e2.nextval = e3
list.listprint()'''


'''class Node:
   def _init_(self, dataval=None):
      self.dataval = dataval
      self.nextval = None
class SLinkedList:
   def _init_(self):
      self.headval = None
   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval
   def AtBegining(self,newdata):
      NewNode = Node(newdata)
      NewNode.nextval = self.headval
      self.headval = NewNode
list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list.headval.nextval = e2
e2.nextval = e3
list.AtBegining("Sun")
list.listprint()'''


'''class Node:
   def _init_(self, dataval=None):
      self.dataval = dataval
      self.nextval = None
class SLinkedList:
   def _init_(self):
      self.headval = None
   def AtEnd(self, newdata):
      NewNode = Node(newdata)
      if self.headval is None:
         self.headval = NewNode
         return
      laste = self.headval
      while(laste.nextval):
         laste = laste.nextval
      laste.nextval=NewNode
   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval
list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list.headval.nextval = e2
e2.nextval = e3
list.AtEnd("Thu")                                       
list.listprint()'''


'''class Node:
   def _init_(self, dataval=None):
      self.dataval = dataval
      self.nextval = None
class SLinkedList:
   def _init_(self):
      self.headval = None
   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval
   def AtBegining(self,newdata):
      NewNode = Node(newdata)
      NewNode.nextval = self.headval
      self.headval = NewNode
list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list.headval.nextval = e2
e2.nextval = e3
list.AtBegining("Sun")
list.listprint()'''


'''class Node:
   def _init_(self, data=None):
      self.data = data
      self.next = None
class SLinkedList:
   def _init_(self):
      self.head = None
   def Atbegining(self, data_in):
      NewNode = Node(data_in)
      NewNode.next = self.head
      self.head = NewNode
   def RemoveNode(self, Removekey):
      HeadVal = self.head
      if (HeadVal is not None):
         if (HeadVal.data == Removekey):
            self.head = HeadVal.next
            HeadVal = None
            return
      while (HeadVal is not None):
         if HeadVal.data == Removekey:
            break
         prev = HeadVal
         HeadVal = HeadVal.next
      if (HeadVal == None):
         return
      prev.next = HeadVal.next
      HeadVal = None
   def LListprint(self):
      printval = self.head
      while (printval):
         print(printval.data),
         printval = printval.next
llist = SLinkedList()
llist.Atbegining("Mon")
llist.Atbegining("Tue")
llist.Atbegining("Wed")
llist.Atbegining("Thu")
llist.RemoveNode("Tue")
llist.LListprint()'''


'''class Node:
    def _init_(self,data):
        self.item = data
        self.ref = None
class linkedlist:
    def _init_(self,):
        self.start_node = None
    def traverse_list(self):
        if self.start_node is None:
            print("List has No element")
        else:
            n=self.start_node
            while n is not None:
                print(n.item,"")
                n=n.ref
    def insert_at_start(self,data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node
    def delete_at_start(self):
        if self.start_node is None:
            print("there is no element to delete")
            return
        self.start_node=self.start_node.ref
    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element")
            return
        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None
new_linked_list = linkedlist()
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(15)
new_linked_list.insert_at_end(20)
new_linked_list.insert_at_end(25)
new_linked_list.insert_at_end(30)
new_linked_list.insert_at_end(35)
new_linked_list.insert_at_end(40)
new_linked_list.insert_at_end(45)
new_linked_list.traverse_list()
new_linked_list.delete_at_start()
print("After deletion at the beginning ")
new_linked_list.traverse_list()
new_linked_list.delete_at_end()
print("After deletion at the end")'''
