class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        N, D = len(nums), len(dp)
        for i in range(1, D):
            for j in range(N):
                if i - nums[j] >= 0:
                    dp[i] += dp[i - nums[j]]

        return dp[target]