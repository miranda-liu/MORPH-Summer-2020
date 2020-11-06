import java.util.ArrayList;

//used for Problems2.java
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(){};
    TreeNode(int val){
        this.val = val;
    }
    TreeNode(int val, TreeNode left, TreeNode right){
        this.val = val;
        this.left = left;
        this.right = right;
    }

    public boolean isLeaf() {
        return this.left == null && this.right == null;
    }

    public ArrayList<Integer> inOrder(TreeNode t){
        ArrayList<Integer> tree = new ArrayList<>();
        if(t.left != null){
            tree.add(t.left.val);
            t.left.inOrder(t.left);
        }
        tree.add(val);

        if(t.right != null){
            tree.add(t.right.val);
            t.right.inOrder(t.right);
        }

    public ArrayList<Integer> preOrder(TreeNode t){
        ArrayList<Integer> tree = new ArrayList<>();
        tree.add(val);

        if(t.left != null){
            tree.add(t.left.val);
            t.left.preOrder(t.left);
        }
        
        if(t.right != null){
            tree.add(t.right.val);
            t.right.preOrder(t.right);
        }
        return tree;
    }
    public ArrayList<Integer> postOrder(TreeNode t){
        ArrayList<Integer> tree = new ArrayList<>();
        if(t.left != null){
            tree.add(t.left.val);
            t.left.inOrder(t.left);
        }
        
        if(t.right != null){
            tree.add(t.right.val);
            t.right.inOrder(t.right);
        }

        tree.add(val);

        return tree;
    }
    private Node addNode(Node current, int value) {
        if (current == null) {
            return new Node(value);
        }
     
        if (value < current.value) {
            current.left = addNode(current.left, value);
        } else if (value > current.value) {
            current.right = addNode(current.right, value);
        } else {
            // value already exists
            return current;
        }
     
        return current;
    }
  
}