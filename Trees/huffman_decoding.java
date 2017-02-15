/*  
   class Node
      public  int frequency; // the frequency of this tree
       public  char data;
       public  Node left, right;
    
*/ 

void decode(String S ,Node root)
    {
       Node iter = root;
    
    for(int i =0 ;i<S.length();++i)
        {
       char k = S.charAt(i);
            if (k=='0')
            iter = iter.left;
            else
            iter = iter.right;
            if(iter.data!='\0')
            {
            System.out.print(iter.data);
                iter = root;
        }
    }

       
    }