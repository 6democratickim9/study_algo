class Solution {
    public void output(List<Integer> out,TreeNode root){

        if(root==null){
            return;
        }
        output(out, root.left);//recursion 쓰거나 inorderTraversal 다시 써도 됨 -> param 수에 따라 맞게 호출
        out.add(root.val);
        output(out, root.right);
    }
    
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> outlist = new ArrayList<Integer>();
        output(outlist,root);
        return outlist;

    }
}