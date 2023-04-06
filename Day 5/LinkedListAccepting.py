class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def merge_lists(list1, list2, n):
    curr_node = list1
    for i in range(n-1):
        curr_node = curr_node.next
        
    next_node = curr_node.next
    curr_node.next = list2
    
    while list2.next:
        list2 = list2.next
    list2.next = next_node
    
    return list1
list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(4)
list1.next.next.next = Node(3)
list1.next.next.next.next = Node(5)
list2 = Node(9)
list2.next = Node(8)
list2.next.next = Node(11)
merged_list = merge_lists(list1, list2, 2)
while merged_list:
    print(merged_list.data, end="->")
    merged_list = merged_list.next
