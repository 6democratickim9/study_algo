public class Main {
	public static void main(String[] args) {
    	System.out.println(isPalindrome("ABCBA"));   // N = 5, N/2 = 2 -> 중앙
    	System.out.println(isPalindrome("ABCCBA"));  // N = 6, N/2 = 3(오른쪽), N/2-1 (왼쪽)
    	System.out.println(isPalindrome("ABA"));
    	System.out.println(isPalindrome("ABBC"));
    	System.out.println(isPalindrome("ABCBa"));
    	System.out.println(isPalindrome("AB!BA"));
    	System.out.println(isPalindrome("ABCABC"));
        System.out.println(isPalindrome("ABCDDCBA"));
    	//   ||
    	// ABCCBA
    	//   |	l <-> r
    	// ABCBA
	}

    static boolean isPalindrome(String str) {
        int cnt=1;
        int n = str.length();
        char[] arr = str.toCharArray();
        for(int i =0;i<n;i++){
            if(n%2==1){
                if(!Character.isAlphabetic(arr[(n/2)])){
                    return false;
                }
            }
            if(!Character.isAlphabetic(arr[i]) || !Character.isAlphabetic(arr[n-1-i]) || !Character.isAlphabetic(arr[(n/2)])){
                return false;
            }
            if(arr[i]!=arr[n-1-i]){
                return false;
            }
            if(cnt==n/2){
                return true;
            }
            cnt++;
        }
    
    // ‘a-z’ ‘A-Z’
    // Character.isAlphabetic
    // Character.isNumber
    // Character.isUpperCase
    // Character.isLowerCase


    return false;
}

}