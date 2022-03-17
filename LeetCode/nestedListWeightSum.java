class Solution {
    
    public int depthSum(List<NestedInteger> nestedList) {
        
        int depth = 1;
        int sum = 0;
        
        if(nestedList == null) return 0;
        
        Queue<NestedInteger> queue = new LinkedList<NestedInteger>(nestedList);
        
        while(!queue.isEmpty()){
            int size = queue.size();
            
            for(int i = 0; i<size; i++){
                NestedInteger neint = queue.poll();
                
                if(neint.isInteger()){
                    sum += neint.getInteger() * depth;
                }else{
                    queue.addAll(neint.getList());
                }
                
            }
            depth++;
        }
        
        

        
        
        return sum;
    }

}