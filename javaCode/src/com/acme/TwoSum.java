package com.acme;

import java.util.HashSet;
import java.util.Set;

public class TwoSum {

    class Solution {
        public int[] twoSum(int[] nums, int target) {
            if (nums == null) return nums;
            Set<Integer> past = new HashSet<Integer>();
            past.add(nums[0]);
            int[] ret = new int[2];
            int len = nums.length;
            for (int i = 1; i < len; i++) {
                if (past.contains(target - nums[i])) {
                    ret[1] = i;
                    for (int j = 0; j < len; j++) {
                        if (nums[j] == (target - nums[i])) {
                            ret[0] = j;
                            break;
                        }
                    }
                    return ret;
                }
                past.add(nums[i]);
            }
            return nums;
        }
    }
}
