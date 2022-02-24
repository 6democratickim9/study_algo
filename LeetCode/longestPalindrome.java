public class Main {
    public static void main(String[] args) {
        String ans = getLongestPalindrome("ASSDDDDADGTDDDD");
        System.out.println(ans);
    }
    
    static String getLongestPalindrome(String str){
        ArrayList<String> strings = new ArrayList<String>();
        ArrayList<String> palins = new ArrayList<String>();
        HashMap cntidx = new HashMap();
        
        for(int i =0;i<str.length();i++){
            int idx = (int)str.charAt(i);
            if(cntidx.containsKey(idx)){
                String tmp = str.substring((int)cntidx.get(idx),i+1);
                strings.add(tmp);
            }
            else{
                cntidx.put(idx,i);

            }
        }
        
        for(int j=0;j<strings.size(); j++){
            if(isPalindrome(strings.get(j))==false){
                continue;
            }else{
                palins.add(strings.get(j));
            }
        }
        String max = palins.get(0);
        ArrayList<Integer> len = new ArrayList<>();
        for(int k=0; k<palins.size();k++){
            if(palins.get(k).length()>max.length()){
                max = palins.get(k);
            }
        }

        return max;


    }
    
        static boolean isPalindrome(String str) {
        int cnt=1;
        int n = str.length();
        char[] arr = str.toCharArray();
        for(int i = 0; i<n; i++){
            if(arr[i]!=arr[n-1-i]){
                return false;
            }
            if(cnt==n/2){
                return true;
            }
            cnt++;
        }
            return false;
    }
}