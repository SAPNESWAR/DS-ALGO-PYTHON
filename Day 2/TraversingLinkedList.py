#Traversing a linked list


class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class SLinkedList:
    def __init__(self):
        self.headval=None

    def listprint(self):
        printval=self.headval  #1000
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval


    def AtBegining(self,newdata):
        NewNode=Node(newdata)
        #Update the new nodes next val to existing node
        NewNode.nextval=self.headval
        self.headval=NewNode

    #Function to add newnode
    def AtEnd(self,newdata):
        NewNode=Node(newdata)
        if self.headval is None:
            self.headval=NewNode
            return
        laste=self.headval #laste=1000
        while(laste.nextval): #3000
            laste=laste.nextval #3000
        laste.nextval=NewNode

    #inbetween Function to add node
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode=Node(newdata)
        NewNode.nextval=middle_node.nextval
        middle_node.nextval=NewNode

        
list=SLinkedList()
list.headval=Node("Mon") #1000
e2=Node("Tue") #2000
e3=Node("Wed") #3000
#link first Node to second node
list.headval.nextval=e2
#link second node to third node
e2.nextval=e3
list.AtBegining("Sun")
list.AtEnd("Thu")
list.Inbetween(list.headval.nextval.nextval.nextval,"Fri")
list.listprint()

