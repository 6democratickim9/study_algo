import java.util.List;

class Solution {
    public int[] twoSum(int[] nums, int target) {

        int[] answer = new int[2];

        for (int a = 0; a < nums.length; a++) {
            for (int i = a + 1; i < nums.length; i++) {
                if (nums[a] + nums[i] == target) {
                    answer[0] = a;
                    answer[1] = i;
                }
            }
        }
        return answer;
    }
}