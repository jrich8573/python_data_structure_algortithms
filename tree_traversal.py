# tree traversal

class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key
        
def printInOrder(root):
        
    if root:
        printInOrder(root.left)
            
        print(root.val, end = " "),
            
        printInOrder(root.right)
            
            
if __name__=="__main__":
    root = Node(1)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)
    root.right.right = Node(2)
    
    print("The order of Traversal of a binary tree: ")
    printInOrder(root)
    