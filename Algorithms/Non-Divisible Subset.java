import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the nonDivisibleSubset function below.
    static int nonDivisibleSubset(int k, int[] S) {
        int freqRemainders[]=new int[k+1];//last elem. is there only so that line 24 works
        int count=0;
        for(int i=0;i<S.length;i++)
            freqRemainders[S[i]%k]++;
        
        int cond=(k%2==0)?k/2:(k/2)+1;
       for(int j=0;j<cond;j++)
       {
           if(freqRemainders[0]!=0&&j==0)
               count++;
           else
           count+=(freqRemainders[j]>freqRemainders[k-j])?freqRemainders[j]:freqRemainders[k-j];
       }
       if(k%2==0)
           count++;
        return count;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] nk = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nk[0]);

        int k = Integer.parseInt(nk[1]);

        int[] S = new int[n];

        String[] SItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int SItem = Integer.parseInt(SItems[i]);
            S[i] = SItem;
        }

        int result = nonDivisibleSubset(k, S);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
