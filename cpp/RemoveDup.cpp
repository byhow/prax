// 26. Remove Duplicates from Sorted Array
// in place swap with current index
#include <vector>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
        int i = 0;
        int len = nums.size();

        if (len < 2)
            return len;

        for (int j = 1; j < len; j++) {
            if (nums[i] != nums[j])
                nums[++i] = nums[j];
        }

        return i + 1;
        
    }
};