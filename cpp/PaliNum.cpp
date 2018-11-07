#include <string>

class Solution {
public:
    bool isPalindrome(int x) {
        auto s = std::to_string(x);
        std::string new_str = "";
        int len = s.length();
        for (int i = len - 1; i > -1; i--) {
            new_str += s[i];
        }
        return true ? new_str == s : false;
        
    }
};