import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    static String[] finalGrid(int[][] matrix, String[] grid) {
		//back to string
    	String[] newGrid=new String[grid.length];
    	for(int i=0;i<grid.length;i++)
    	{
    		newGrid[i]="";
    		for(int j=0;j<grid[0].length();j++)
    		{
    			if(matrix[i][j]<-50)
    				newGrid[i]+=".";
    			else
    				newGrid[i]+="O";
    		}
    	}
    	return newGrid;
	}
	
	static String[] fullGrid(String[] grid) {
		String[] newGrid=new String[grid.length];
		for(int i=0;i<grid.length;i++)
		{
			newGrid[i]="";
			for(int j=0;j<grid[i].length();j++)
				newGrid[i]+="O";
		}
		return newGrid;
	}

	static int[][] A;
	static int[][] B;
	
	// Complete the bomberMan function below.
    static String[] bomberMan(int n, String[] grid) {
    	// translate into int
    	int[][] matrix=new int[grid.length][grid[0].length()];
    	for(int i=0;i<grid.length;i++)
    	{
    		for(int j=0;j<grid[0].length();j++)
    		{
    			if(grid[i].charAt(j)=='.')
    				matrix[i][j]=-99;
    			else
    				matrix[i][j]=2;
    		}
    	}
    	if(n==1)
            return grid;
    	//printM(matrix);
    	
    	// now real deal starts
    	int howManyTimesOdd=0;
    	for(int who=1;who<=n;)
    	{
    	//decrease all of 1 and fill empty
    	for(int i=0;i<grid.length && B==null;i++)
    	{
    		for(int j=0;j<grid[0].length();j++)
    		{
    			matrix[i][j]--;
    			if(matrix[i][j]<-50)
    				matrix[i][j]=3;
    		}
    	}
    	
    	//printM(matrix);
    	who++;
    	if(who==n)
    		return fullGrid(grid);
    	
    	//wait for them to explode
    	for(int i=0;i<grid.length && B==null;i++)
    	{
    		for(int j=0;j<grid[0].length();j++)
    		{
    			matrix[i][j]--;
    			if(matrix[i][j]==0)
    			{
    				//make cross clear
    				if(i>0 && matrix[i-1][j]>1)
    					matrix[i-1][j]=-99;
    				if(j>0 && matrix[i][j-1]>1)
    					matrix[i][j-1]=-99;
    				if(i<grid.length-1 && matrix[i+1][j]>1)
    					matrix[i+1][j]=-99;
    				if(j<grid[0].length()-1 && matrix[i][j+1]>1)
    					matrix[i][j+1]=-99;
    				matrix[i][j]=-99;
    			}
    		}
    	}
    	
    	//printM(matrix);
    	howManyTimesOdd++;
    	if(A==null)
    	{
    		A=new int[matrix.length][matrix[0].length];
    		for(int i=0;i<matrix.length;i++)
    			for(int j=0;j<matrix[0].length;j++)
    				A[i][j]=matrix[i][j];
    	}
    	else if(B==null)
    	{
    		B=new int[matrix.length][matrix[0].length];
    		for(int i=0;i<matrix.length;i++)
    			for(int j=0;j<matrix[0].length;j++)
    				B[i][j]=matrix[i][j];
    	}
    	who++;
    	if(who==n)
    	{
    		if(howManyTimesOdd%2==1)
    			return finalGrid(A, grid);
    		else
    			return finalGrid(B, grid);
    	}
    	}
    	return null;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] rcn = scanner.nextLine().split(" ");

        int r = Integer.parseInt(rcn[0]);

        int c = Integer.parseInt(rcn[1]);

        int n = Integer.parseInt(rcn[2]);

        String[] grid = new String[r];

        for (int i = 0; i < r; i++) {
            String gridItem = scanner.nextLine();
            grid[i] = gridItem;
        }

        String[] result = bomberMan(n, grid);

        for (int i = 0; i < result.length; i++) {
            bufferedWriter.write(result[i]);

            if (i != result.length - 1) {
                bufferedWriter.write("\n");
            }
        }

        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
