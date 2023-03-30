class Node:
    def __init__(self,value):
        self.previous=None
        self.data=value
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def length(self):
        temp = self.head
        count=0
        while temp is not None:
            temp = temp.next
            count+=1
        return count

    def insertAtBeginning(self,value):
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.data,sep=",")
            temp = temp.next

    def insertAtEnd(self,value):
        new_node = Node(value)
        if self.isEmpty():
            self.insertAtBeginning(value)
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next = new_node
            new_node.previous = temp
    
    def insertAtPosition(self,value,position):
        temp= self.head
        count=1
        while temp is not None:
            if count == position-1:
                break
            count+=1
            temp=temp.next
        if position==1:
            self.insertAtBeginning(value)
        elif temp is None:
            print("there are less than {}-1 elements in the linked list")
        elif temp.next is None:
            self.insertAtEnd(value)
        else:
            new_node = Node(value)
            new_node.next=temp.next
            new_node.previous=temp
            temp.next.previous=new_node
            temp.next = new_node

x = DoublyLinkedList()
print(x.isEmpty())
# x.insertAtBeginning(5)
# x.printLinkedList()
# x.insertAtBeginning(15)
# x.insertAtBeginning(25)
# x.printLinkedList()
# print("no. of nodes",x.length())


x.insertAtEnd(5)
x.insertAtEnd(15)
x.insertAtEnd(25)
x.insertAtEnd(35)
x.printLinkedList()
print("no. of nodes",x.length())
