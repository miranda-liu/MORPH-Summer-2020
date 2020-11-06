public class Tree {
    Nodes root;
    public Tree(int value){
        root = new Nodes(value);
    }
    
    public static void main(String[] args) {
        Tree t1 = new Tree(1);
        System.out.println(t1.root.value);
        //System.out.println(t1.root.child1.value);
        Nodes c1 = new Nodes(3);
        t1.root.child1 = c1;
        System.out.println(t1.root.child1.value);
    }
    
    public void inOrder(Tree t){
        //first check if root is null
        if(t.root == null){
            return;
        }
        //left child
   
        inOrder(new Tree(t.root.child1.value));
        
        
        //root
        System.out.println(t.root.value);
        //right child
        inOrder(new Tree(t.root.child2.value));

        /*
                    1
                   / \
                  2   3
                 /
                4
            Output: 2, 1, 3
        */

    }
}