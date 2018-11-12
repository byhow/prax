#include <string>
#include <unordered_set>
#include <iostream>

class Solution {
public:
    int numJewelsInStones(std::string J, std::string S) {
        std::unordered_set<char> mySet = {}; 
        int len = J.length();
        for (int i = 0; i < len; i++) {
            mySet.insert(J[i]);   
        }
        int count = 0;
        for (auto it = S.begin(); it < S.end(); ++it) {
            if (mySet.count(*it)) {
                count++;
            }
        }
        return count;
    }
};
