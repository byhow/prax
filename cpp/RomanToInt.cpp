#include <unordered_map>
#include <string>
#include <iostream>
using namespace std;


class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> um({
            {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50},
            {'C', 100}, {'D', 500}, {'M', 1000} });
        
        int sum = 0;
        size_t len = s.length();
        
        for (int i = 0; i < len; ++i) {
            if (s[i] == 'I') {
                if (i + 1 < len && (s[i + 1] == 'V' || s[i + 1] == 'X')) {
                    sum += um[s[++i]] - 1;
                } else {
                    sum += um[s[i]];
                }
            } else if (s[i] == 'X') {
                if (i + 1 < len && ((s[i + 1] && s[i + 1] == 'L') || s[i + 1] == 'C')){
                    sum += um[s[++i]] - 10;
                } else {
                    sum += um[s[i]];
                }
            } else if (s[i] == 'C') {
                if (i + 1 < len && ((s[i + 1] && s[i + 1] == 'D') || s[i + 1] == 'M')) {
                    sum += um[s[++i]] - 100;
                } else {
                    sum += um[s[i]];
                }
            } else {
                sum += um[s[i]];
            }
        }
        
        return sum;
    }
};


int main() {
    Solution s;
    cout << s.romanToInt("III") << endl;
    return 0;
}


