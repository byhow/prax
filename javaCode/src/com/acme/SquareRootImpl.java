package com.acme;

public class SquareRootImpl {
    public int mySqrt(int x) {
        if (x == 0) return x;
        int lo = 1, hi = x / 2 + 1;

        while (lo + 1 < hi) {
            int mid = (lo + hi) / 2;

            if (mid > x / mid) {
                hi = mid;
            } else if(mid < x / mid) {
                lo = mid;
            } else {
                return mid;
            }

        }

        return lo;
    }
}
