import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {
static int equalsChars=0;
	static int lastCompareOutput=2;
    // Complete the morganAndString function below.
    static String morganAndString(String a, String b) {
        a+="z";b+="z";
        StringBuilder sb=new StringBuilder();
        int n=a.length()+b.length();
        int indexB=0, indexA=0;

        for(int i=0;i<n-2;i++)
        {
            if(aCompareB(a,b, indexA, indexB)>0)
            {
                sb.append(b.charAt(indexB));
                //b.deleteCharAt(0);
                if(equalsChars--==0)
                	equalsChars=0;
                indexB++;
            }
            else
            {
                sb.append(a.charAt(indexA));
                //a.deleteCharAt(0);
                if(equalsChars--==0)
                	equalsChars=0;
                indexA++;
            }
        }
        return sb.toString();
    }
	
	static int aCompareB(String a, String b, int indexA, int indexB) {
		if(equalsChars>0)
			return lastCompareOutput;
		int n=Math.max(a.length(), b.length());
		boolean counting=true;
		for(int i=0;i<n;i++)
		{
			if(a.charAt(i+indexA)=='z')
			{
				lastCompareOutput=1;
				return 1;
			}
			if(b.charAt(i+indexB)=='z')
			{
				lastCompareOutput=-1;
				return -1;
			}
			if(a.charAt(i+indexA)>b.charAt(i+indexB))
			{
				lastCompareOutput=1;
				return 1;
			}
			if(a.charAt(i+indexA)<b.charAt(i+indexB))
			{
				lastCompareOutput=-1;
				return -1;
			}
			if(a.charAt(indexA+i)==a.charAt(indexA+i+1) && counting)
				equalsChars++;
			if(a.charAt(indexA+i)!=a.charAt(indexA+i+1))
				counting=false;
		}
		return 0/0;
	}

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            String a = scanner.nextLine();

            String b = scanner.nextLine();

            String result = morganAndString(a, b);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }
        bufferedWriter.close();

        scanner.close();
    }
}
