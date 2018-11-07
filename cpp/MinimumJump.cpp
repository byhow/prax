// BFS search for node on level, which is the number of leaps

#include <vector>
using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int len = nums.size();
        if (len < 2) return 0;

        int i = 0, currentMax = 0, nextMax = 0, layer = 0;

        while (i <= currentMax) {
            ++layer;

            for (; i <= currentMax; i++) {
                nextMax = max(nextMax, nums[i] + i);
                if (nextMax >= len - 1) return layer;
            }
            currentMax = nextMax;
        }

        return -1;
    }
};