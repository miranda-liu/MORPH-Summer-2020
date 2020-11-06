public class CorrectTree {
    private int value;
    private CorrectTree childLeft = null;
    private CorrectTree childRight = null;

    public CorrectTree(int value) {
        this.value = value;
    }

    public void inOrderSearch(CorrectTree tree) {
        if (tree == null) {
            return;
        }

        this.inOrderSearch(tree.childLeft);

        System.out.println(tree.value);

        this.inOrderSearch(tree.childRight);
    }
}