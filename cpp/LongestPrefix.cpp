#include <string>
#include <vector>
using namespace std;
class Solution {
    // confusing and hard

    public:
        string longestCommonPrefix(vector<string>& strs) {
            int size = strs.size(), min_length, j = 0, i = 0;

            if (size == 0) return "";
            if (size == 1) return strs[0];
            string com = "";
            min_length = strs[0].size();
            
            for(; i < size; i++) {
                if(strs[i].size() < min_length) min_length = strs[i].size();
            }

            for(; j != min_length; j++) {
                for (i = 1; i != size; i++) {
                    if (strs[0][j] != strs[i][j]) break;
                }
                if (i != size) break;
            }

            for (i = 0; i != j; ++i) {
                com += strs[0][i];
            }

            return com;
        }
};