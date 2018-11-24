#include <string>
#include <vector> 
#include <iostream>
using namespace std;

/** 
 * KMP implementation with Partial Match Table
 * Still confusing, but got the general ideas
 */
class Solution {
public:
    int strStr(string haystack, string needle) {
        int lenH = haystack.length(), lenN = needle.length();
        if (!lenN) return 0;
        vector<int> lps = kmp(needle);
        
        for (int i = 0, j = 0; i < lenH; ) {
            if (haystack[i] == needle[j]) {
                i++; j++;
            } 
            if (j == lenN) return i - j;

            if ((i < lenH) && (haystack[i] != needle[j])) {
                if (j) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }

        return -1;
    }


    vector<int> kmp(string& needle) {
        int n = needle.length();
        vector<int> lps(n, 0);
        for (int i = 1, sub = 0; i < n; ) {
            if (needle[i] == needle[sub]) {
                lps[i++] = ++sub;
            } else if (sub) {
                sub = lps[sub - 1];
            } else {
                lps[i++] = 0;
            }
        }
        return lps;
    }
};


int main(){
    Solution s;
    s.strStr("aaaa", "bba");
}