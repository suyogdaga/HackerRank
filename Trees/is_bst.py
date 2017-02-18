int_min=0
int_max=10000
class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def isBST(node):
    return(isBSTUTIL(node,int_min,int_max))

def isBSTUTIL(node,mini,maxi):
    if node is None:
        return True
    if node.data<mini or node.data>maxi:
        return False
    
    return(isBSTUTIL(node.left,mini,node.data-1) and 
            isBSTUTIL(node.right,mini,node.data+1))

root = Node(4)
root.left = Node(2)
root.rigt = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

if (isBST(root)):
    print "Is BST"
else:
    print "Not a BST"