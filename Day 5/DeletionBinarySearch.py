# Binary search tree operation in python
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key) + "->", end=' ')
        inorder(root.right)

# insert a node
def insert(node,key):
    # return a new node if the tree is empty
    if node is None:
        return Node(key)
    # traverse to the right place and insert the node
    if key < node.key:
        node.left = insert(node.left,key)
    else:
        node.right = insert(node.right,key)
    return node

# find the inorderSuccessor
def minvalueNode(node):
    current=node
    # find the leftmost leaf
    while(current.left is not None):
        current = current.left
    return current

# Deleting Node
def deleteNode(root,key):
    if root is not None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left,key)
    elif key > root.key:
        root.right = deleteNode(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root - None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minvalueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right,temp.key)
    return root

root = None
root = insert(root,8)
root = insert(root,3)
root = insert(root,1)
root = insert(root,6)
root = insert(root,7)
root = insert(root,10)
root = insert(root,14)
root = insert(root,4)
print("Inorder Traversal: ",end='')
inorder(root)
