   /* 
    
    class Node 
       int data;
       Node left;
       Node right;
   */
   void LevelOrder(Node root)
{
	int h = height(root) ;
	int i;
	for (i=1;i<=h;i++)
		printGivenLevel(root,i);

      
}

int height(Node root)
{
	if (root ==null)
	{
		return 0;
	}
	else
	{
		int left = height(root.left);
		int right = height(root.right);

		if(left > right)
			return(left +1);
		else
			return(right+1);
	}
}

void printGivenLevel (Node root ,int level)
    {
        if (root == null)
            return;
        if (level == 1)
            System.out.print(root.data + " ");
        else if (level > 1)
        {
            printGivenLevel(root.left, level-1);
            printGivenLevel(root.right, level-1);
        }
    }
