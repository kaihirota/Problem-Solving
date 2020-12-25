import java.util.*;
import java.io.*;

public class ATM {
    public static void main(String[] args) {
        Scanner input = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int numCases = input.nextInt();
        for(int t=1; t<numCases+1; t++) {
            int n = input.nextInt();
            int limit = input.nextInt();
            ArrayList<Integer> arr = new ArrayList<>();
            ArrayList<Integer> idx = new ArrayList<>();
            ArrayList<String> tmp = new ArrayList<>(Arrays.asList(input.nextLine().split(" ")));

            for(int i=1; i<n+1; i++) {
                arr.add(Integer.parseInt(tmp.get(i-1)));
                idx.add(i);
            }

            for(int i: arr) System.out.println(i);
            for(int i: idx) System.out.println(i);

            // p("Case #" + caseId + ": " + ans);
        }
    }

    private static void p() {
        p("");
    }

    private static void p(String s) {
        System.out.println(s);
    }
}
