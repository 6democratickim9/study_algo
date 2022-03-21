class Solution {
    public boolean solution(int[] arr, int n) {
        HashMap counts = new HashMap();
        int[] answer = new int[2];
        for (int a = 0; a < nums.length; a++) {
            int tmp = target - nums[a];
            counts.put(tmp,a);
        }

        for (int b = 0; b < nums.length; b++) {
            try{  
                if (counts.containsKey(nums[b]) && !(counts.get(nums[b])).equals(b)) {
                answer[0] = (int)counts.get(nums[b]);
                answer[1] = b;
            }
               }
            catch(Exception e)
            {
                continue;
            }
          

        }
        return answer;

    }
}