class MyStack {

    public MyStack() {
        myQueue1 = new LinkedList<>();
        myQueue2 = new LinkedList<>();
        
    }
    
    public void push(int x) {
        myQueue1.offer(x);
        if(myQueue1.size()>1){
            while(myQueue1.size()>1){
                myQueue2.add(myQueue1.poll());
            }
            while(!myQueue2.isEmpty()){
                myQueue1.add(myQueue2.poll());
            }
        }
            
    }
    
    public int pop() {
        return myQueue1.poll();
        
    }
    
    public int top() {
        return myQueue1.peek();
        
    }
    
    public boolean empty() {
        return myQueue1.isEmpty();   
    }
        Queue<Integer> myQueue1;
        Queue<Integer> myQueue2;
}