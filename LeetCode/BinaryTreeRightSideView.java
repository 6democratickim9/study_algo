class Solution {
    
    public void putRightSide(List<Integer> list, TreeNode root, int currDepth){
        if(root!=null){

            if(list.size()==currDepth){
                list.add(root.val);
            }
            putRightSide(list, root.right, currDepth+1);
            putRightSide(list, root.left, currDepth+1);
        }
        return;
    
    }
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> list = new ArrayList<Integer>();
        putRightSide(list,root,0);
        return list;
    }
    
}