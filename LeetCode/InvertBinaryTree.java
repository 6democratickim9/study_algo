class Solution {
    public TreeNode invertTree(TreeNode root) {
        if(root==null) return null;
        TreeNode rootRight = invertTree(root.right);
        TreeNode rootLeft = invertTree(root.left);
        root.right = rootLeft;
        root.left = rootRight;
        return root;
    }