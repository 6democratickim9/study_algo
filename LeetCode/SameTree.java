class Solution{//Recursion 가장 첫번째 statement는 종료 조건 이어야 함 -> 호출 전에 종료를 체크해야 함
    public boolean isSameTree(TreeNode p, TreeNode q) {
        isSameTree(p.left,q.left);
        if(p==null&&q==null){//address를 가리키고 있음 -> 같은 결과가 반환될 수 없음
            return true;
        }if(p==null || q==null){//null check가 필요한 이유 -> 
            return false;
        }else if(p.val!=q.val){
            return false;
        }
    return  isSameTree(p.right,q.right);
    }

}