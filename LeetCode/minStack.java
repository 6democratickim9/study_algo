class MinStack {
    Stack<Integer> minStack;
    Stack<Integer> min;

    public MinStack() {
        minStack = new Stack<Integer>();
        min = new Stack<Integer>();
    }

    public void push(int val) {
        if (min.isEmpty() == true) {
            min.push(val);
        } else if (min.peek() >= val) {
            min.push(val);
        }
        minStack.push(val);

    }

    public void pop() {

        if (minStack.pop().equals(min.peek())) {
            min.pop();
        }
    }

    public int top() {
        return minStack.peek();

    }

    public int getMin() {
        return min.peek();

    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */