"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    if head:
        k = 0
        if position == k:
            head = head.next
        else:
            temp = head
            prev = temp
            while k!= position :
                prev = temp
                temp = temp.next
                k = k+1
            prev.next = temp.next
    else:
        return
    return head
  
  
  
  
