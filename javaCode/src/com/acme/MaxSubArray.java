package com.acme;

public class MaxSubArray {
    public int maxSubArray(int[] nums) {
        int prev = Integer.MIN_VALUE;
        int sum = 0;

        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            prev = sum > prev ? sum : prev;
            sum = sum > 0 ? sum : 0;
        }

        return prev;
    }
}
