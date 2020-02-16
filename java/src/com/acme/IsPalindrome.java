package com.acme;

public class IsPalindrome {
    public boolean isPalindrome(int x) {
        if (x < 10 && x >= 0) return true;
        if (x < 0) return false;

        int rev = 0;
        int cpy_digit = x;
        int cpy = x;
        long counter = 1;

        while (cpy_digit != 0) {
            cpy_digit /= 10;
            counter *= 10;
        }
        counter /= 10;

        while (cpy != 0) {
            int remi = cpy % 10;
            rev += remi * counter;
            // System.out.println(rev);

            counter /= 10;
            cpy /= 10;
            // System.out.println(counter);
            // System.out.println(cpy);
        }

        return x == rev;
    }

    public static void main(String[] args) {
        IsPalindrome IP = new IsPalindrome();
        System.out.println(IP.isPalindrome(1000000001));
    }
}


