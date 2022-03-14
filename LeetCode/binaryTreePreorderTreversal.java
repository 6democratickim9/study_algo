class Solution {
    public void output(List<Integer> out, TreeNode root) {
        if (root != null) {
            out.add(root.val);
            output(out, root.left);

            output(out, root.right);
        }
    }

    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> outlist = new ArrayList<Integer>();
        output(outlist, root);
        return outlist;
    }
}