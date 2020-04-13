#include <vector>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int len = nums.size();
        int dp[len];
        dp[0] = nums[0];
        int max = dp[0];
        for (int i = 1; i<len; i++) {
            dp[i] = nums[i] + (dp[i-1]>0? dp[i-1]:0);
            max = max>dp[i]? max:dp[i];
        }
        return max;
    }
};