import java.util.ArrayList;

//uses TreeNode.java
public class Problems2 {
    public static void main(String[] args) {
    }

   
    }
    public boolean isSameTree(TreeNode p, TreeNode q){
       ArrayList<Integer> pList = new ArrayList<>();
       pList = p.preOrder(p);

       ArrayList<Integer> qList = new ArrayList<>();
       qList = q.preOrder(q);

       return pList.equals(qList);
    }

    public boolean hasPathSum(TreeNode root, int sum){
        boolean found = false;
        this.hasPathSumHelper(root, 0, sum, found);
        return found;
    }

    private void hasPathSumHelper(TreeNode node, int sum, int goal, boolean found){
        if(node == null){
            return;
        }
        if(node.isLeaf()){
            found = found || sum + node.val == goal;
            return;
        }
        else{
            sum += node.val;
            hasPathSumHelper(node.left, sum, goal, found);
            hasPathSumHelper(node.right, sum, goal, found);
        }
    }

    public TreeNode buildTree(int[] preorder, int[] inorder){
        int indexRootInorder = 0;
        TreeNode root = new TreeNode(preorder[indexRootInorder]);
        for(int i = 0; i < inorder.length; i++){
            if(inorder[i] == root.val){
                indexRootInorder = i;
            }
        }
        for(int i = 0; i < indexRootInorder; i++){

        }
        
    }

    public void traverse_BFS(TreeNode node){
        /* 1. check if the node is null and exit if null
           2. print the values of all the children
           3. call each of the node's children
        */
        if(node == null){
            return;
        }
        System.out.println(node.left.val);
        System.out.println(node.right.val);

        traverse_BFS(node.left);
        traverse_BFS(node.right);
    }

    public void traverse_DFS(TreeNode node){
        /* 1. check if the node is null and exit if null
           2. print the value of the node
           3. call each of the node's children
        */
        if(node == null){
            return;
        }
        System.out.println(node.val);

        traverse_DFS(node.left);
        traverse_DFS(node.right);
    }
}