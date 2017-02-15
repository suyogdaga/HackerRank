 /* Node is defined as :
 class Node 
    int data;
    Node left;
    Node right;
    
    */

static Node Insert(Node root,int value)
    {
       
        Node node = new Node();
        node.data = value;
        if(root==null){
            return node;
        }    
        Node tmp = root;       
        while(tmp!=null){
            if(tmp.data > value){
                if(tmp.left !=null)
                    tmp = tmp.left;
                else{
                    tmp.left = node;
                    break;
                }                    
            }
            else if(tmp.right !=null)
                    tmp = tmp.right;
            else{
                tmp.right = node;
                break;
            }                                   
        }
        return root;       
    
    }


