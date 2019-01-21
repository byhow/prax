package com.acme;

public class ReverseInt {
    public int reverse(int x) {
        long res = 0;

        while (x != 0) {
            res = res * 10 + x % 10;
            x /= 10;
        }

        if (res > Integer.MAX_VALUE || res < Integer.MIN_VALUE) return 0;
        return (int) res;

    }
    public static void main(String[] args) {
        ReverseInt IP = new ReverseInt();
        System.out.println(IP.reverse(1534236469));
    }
}
