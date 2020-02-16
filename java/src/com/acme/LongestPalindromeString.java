package com.acme;

public class LongestPalindromeString {
    public String longestPalindrome(String s) {
        String ret = "";
        int n = s.length();

        boolean[][] dp = new boolean[n][n];


        for (int i = n - 1; i >= 0 ; i--) {
            for (int j = i; j < n; j++) {

                dp[i][j] = (s.charAt(i) == s.charAt(j) && (j - i < 3 || dp[i + 1][j - 1]));
                if (dp[i][j] && (ret == "" || j - i + 1 > ret.length())) {
                    ret = s.substring(i, j + 1);
                }
            }
        }

        return ret;
    }

    public static void main(String[] args) {
        LongestPalindromeString lps = new LongestPalindromeString();
        String test  = lps.longestPalindrome("babad");
    }
}


