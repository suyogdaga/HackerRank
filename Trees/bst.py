class Node :
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(root,node):
    if root == None:
        root = node
    else:
        if root.data < node.data:
            if root.right== None:
                root.right = node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left,node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
    
        
def search(root,key):
    if root.data == key or root is None:
        print("found")
        if root.data < key:
            return search(root.right,key)
        if root.data> key:
            return search(root.left,key)
    else:
        print("not found")

r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))
search(r,50)

inorder(r)
        
    
    

