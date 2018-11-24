#include <string>
using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        int len_n = needle.length();
        int len_h = haystack.length();
        if (needle == "" || len_h == 1 && len_n == 1) return 0;

        int index = 0;       
        while (index < len_h) {
            if (haystack[index] == needle[0]) {
                for (int j = index, cur = 0; cur < len_n, j < len_h; j++, cur++) {
                    if (haystack[j] != needle[cur]) {
                        break;
                    } else {
                        if (cur == len_n - 1) {
                            return index;
                        }
                    }  
                }
            }
            index++;
        }

        return -1;
    }
};
