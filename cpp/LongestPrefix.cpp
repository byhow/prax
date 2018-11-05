#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int size = strs.size(), max_length = 0, j = 0;

        if (size == 0) return "";
        if (size == 1) return strs[0];
        string com = "";
        
        for(int i = 0; i < size; i++) {
            if(strs[i].size() > max_length) max_length = strs[i].size();
        }

        for(; j != max_length; j++) {
            
        }


        return com;
    }
};