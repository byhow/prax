package com.acme;

public class HourglassSum {
    static int hourglassSum(int[][] arr) {
        int row = arr.length, col = arr[0].length;
        int ms = Integer.MIN_VALUE;
        for (int i = 1; i < row - 1; i++){
            for (int j = 1; j < col - 1; j++){
                int k = arr[i - 1][j-1] + arr[i-1][j]+arr[i-1][j+1]+
                        arr[i][j]+arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1];
                if (k > ms) ms = k;
            }
        }
        return ms;
    }
}
