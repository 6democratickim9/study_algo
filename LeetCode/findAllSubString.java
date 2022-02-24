public class Main {
    public static void main(String[] args) {
        List<String> res = getAllSubstrings("ABCD");
            for (String s : res) {
                System.out.println(s);
            }

    }
    static List<String> getAllSubstrings(String str) {
        ArrayList<String> strings = new ArrayList<String>();
        for(int i=0;i<str.length();i++){
            for(int j=i+1; j<str.length()+1;j++){
                String tmp = str.substring(i,j);
                strings.add(tmp);

            }

        }
        return strings;
}

}