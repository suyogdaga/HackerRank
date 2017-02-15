void top_view(Node root)
{
   topl(root.left);
   System.out.print(root.data+" ");
   topr(root.right);
    
}
void topl(Node root)
    {
    if(root!=null)
        {
        topl(root.left);
        System.out.print(root.data+" ");
    }
}
void topr(Node root){
    if(root!=null)
        {
         System.out.print(root.data+" ");
        topr(root.right);       
    }
}