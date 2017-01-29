"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    new_node = Node(data)
    if head:
        
        k=0 
        if k == position:
            new_node.next = head
            head = new_node
        else:
            node = head
            prev = node
            while(k!=position):
                prev = node
                node = node.next
                k = k+1
            prev.next = new_node
            new_node.next= node
    else:
        head = new_node
    return head
  