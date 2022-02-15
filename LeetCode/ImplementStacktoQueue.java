class MyQueue {

    
    public MyQueue() {
    stack1 = new Stack<>();
    stack2 = new Stack<>();
    }
    
    public void push(int x) {
        stack2.push(x);
        if(stack2.size()>1){
            int tmp = stack2.pop();
            while(!stack2.empty()){
                stack1.push(stack2.pop());
            }
            stack2.push(tmp);
            while(!stack1.empty()){
                stack2.push(stack1.pop());
            }
        }
    }
    
    
    public int pop() {
        return stack2.pop();
    }
    
    public int peek() {
        return stack2.peek();
    }
    
    public boolean empty() {
        return stack2.empty();
        
    }
    Stack<Integer> stack1;
    Stack<Integer> stack2; 
}
