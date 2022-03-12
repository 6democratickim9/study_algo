class Solution {
    
    
    public int rangeSumBST(TreeNode root, int low, int high) {
        ArrayList<Integer> num = new ArrayList<Integer>(); //object 타입
        //num의 메모리 주소를 넘긴것이라서 가능
        //메모리에 추가한것이라서 추가된 것
        
        int[] sum = new int[]{0};//오브젝트라서 가능. 레퍼런스라서!
        //int array는 클래스
        //원본의 메모리 주소값을 복사한 것
        
        findNumInRange(root, low, high, sum);
        
        // 왜 List는 void로 리턴해도 값이 나오는데
        // int는 void로 리턴하면 값이 담기지 않는지?
        
        return sum[0];
    }
    
        public void findNumInRange(TreeNode root, int low, int high, int[] sum){
            
        // java는 int -> primitive 라서 값을 넘기면 값만 넘어감(int 타입이 넘어가는것이 아님)
        // 값만 증가되고 끝남. 위로 리턴되지 않음
        // output parameter의 reference나 pointer로 가능하지만 자바는 pass by value라서 integer 값만 넘어감
        // 트리 노드는 루트의 레퍼런스를 가지고 있어서 가능(메모리 주소)
            
        if(root == null) return;
        findNumInRange(root.left, low, high, sum);
        findNumInRange(root.right, low, high, sum);
            
        if(root.val >= low && root.val <= high){
            sum[0] = sum[0] + root.val;
            //원본 array 값 업데이트
            //pass by value/ pass by reference 찾아보기
        }
        
    }
}