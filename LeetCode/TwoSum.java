import java.util.HashMap;

// import java.util.List;

// class Solution {
//     public int[] twoSum(int[] nums, int target) {

//         int[] answer = new int[2];

//         for (int a = 0; a < nums.length; a++) {
//             for (int i = a + 1; i < nums.length; i++) {
//                 if (nums[a] + nums[i] == target) {
//                     answer[0] = a;
//                     answer[1] = i;
//                 }
//             }
//         }
//         return answer;
//     }
// }

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap counts = new HashMap();
        int[] answer = new int[2];
        for (int a = 0; a < nums.length; a++) {
            int tmp = target - nums[a];
            counts.put(tmp, a);
        }

        for (int b = 0; b < nums.length; b++) {
            try {
                if (counts.containsKey(nums[b]) && !(counts.get(nums[b])).equals(b)) {
                    answer[0] = (int) counts.get(nums[b]);
                    answer[1] = b;
                }
            } catch (Exception e) {
                continue;
            }

        }
        return answer;

    }
}
