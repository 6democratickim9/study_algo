class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> answer = new ArrayList<>();
        makeOrder(answer, root, 0);
        return answer;
    }
    public void makeOrder(List<List<Integer>> list, TreeNode root, int currDepth){
        if(root!=null){
            if(list.size()==currDepth){
                List<Integer> tmp1 = new ArrayList<>();
                tmp1.add(root.val);
                list.add(tmp1);
            }
            else if(list.get(currDepth)!=null){
                List<Integer> tmp2 = list.get(currDepth);
                tmp2.add(root.val);
                list.remove(currDepth);
                list.add(currDepth,tmp2);
            }
            makeOrder(list, root.left, currDepth+1);
            makeOrder(list, root.right, currDepth+1);
        }
        return;
    }
}