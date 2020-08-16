import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the matrixRotation function below.
    static void matrixRotation(int[][] matrix, int r) {
		int h=matrix[0].length;
		int v=matrix.length;

		for(int i=0;i<h-1 && i<v-1;i++)
		{
            for(int rots=0;rots<r%((h-i)*2+2*(v-i)-4);rots++)
			{
                int topLeft=matrix[i][i];
                for(int q=i;q<h-1;q++)
                    matrix[i][q]=matrix[i][q+1];
                for(int q=i;q<v-1;q++)
                    matrix[q][h-1]=matrix[q+1][h-1];
                for(int q=h-1;q>i;q--)
                    matrix[v-1][q]=matrix[v-1][q-1];
                for(int q=v-1;q>i;q--)
                    matrix[q][i]=matrix[q-1][i];
                matrix[i+1][i]=topLeft;
            }
			h--;
			v--;
		}
		

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        String[] mnr = scanner.nextLine().split(" ");

        int m = Integer.parseInt(mnr[0]);

        int n = Integer.parseInt(mnr[1]);

        int r = Integer.parseInt(mnr[2]);

        int[][] matrix = new int[m][n];

        for (int i = 0; i < m; i++) {
            String[] matrixRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < n; j++) {
                int matrixItem = Integer.parseInt(matrixRowItems[j]);
                matrix[i][j] = matrixItem;
            }
        }
        	matrixRotation(matrix, r);
        for(int i=0;i<matrix.length;i++)
		{
			for(int j=0;j<matrix[0].length;j++)
				System.out.print(matrix[i][j]+" ");
			System.out.println();
		}

        scanner.close();
    }
}
