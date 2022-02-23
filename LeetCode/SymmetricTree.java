class Solution {
    public boolean isSymmetric(TreeNode root) {
        return isSymmetric(root.left, root.right);
    }
    public boolean isSymmetric(TreeNode root1, TreeNode root2){//boolean 값일때 is 나(is가 제일 많이 쓰임) has로 시작 

        if (root1==null && root2==null) {//띄어쓰기 신경쓰기!!!!
            return true;
        } else if (root1==null || root2==null) {//가독성 
            return false;
        } else if (root1.val != root2.val) {
            return false;
        }
        
        return isSymmetric (root1.left, root2.right) && isSymmetric (root1.right, root2.left);
    }
}