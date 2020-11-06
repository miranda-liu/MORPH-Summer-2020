//BinaryTree and Node are the only two that work properly
public class BinaryTree {
    private Node root;

    /* insertion
    - if the new node's value is lower than the current node's, we go to the left child
    - if the new node's value is greater than the current node's, we go to the right child
    - when the current node is null, we've reached a leaf node and we can insert the new node in that position
    */
    private Node addRecursive(Node current, int value) {
        if (current == null) {
            return new Node(value);
        }
     
        if (value < current.value) {
            current.left = addRecursive(current.left, value);
        } else if (value > current.value) {
            current.right = addRecursive(current.right, value);
        } else {
            // value already exists
            return current;
        }
     
        return current;
    }

    //starts recursion from root node
    public void add(int value) {
        root = addRecursive(root, value);
    }

    //creating the binary tree
    public BinaryTree createBinaryTree() {
        BinaryTree bt = new BinaryTree();
     
        bt.add(6);
        bt.add(4);
        bt.add(8);
        bt.add(3);
        bt.add(5);
        bt.add(7);
        bt.add(9);
     
        return bt;
    }

    //searching: inorder
    
    //searching: postorder

    //searching: preorder


}