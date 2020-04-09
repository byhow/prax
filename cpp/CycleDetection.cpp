// https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_Tortoise_and_Hare
// https://leetcode.com/problems/happy-number/

using namespace std;
class Solution {
public:

    int next_num(int n) {
        int ret = 0;
        while (n) {
            int temp = n % 10;
            ret += temp * temp;
            n /= 10;
        }
        return ret;
    }
    
    bool isHappy(int n)
    {
        int p1 = n, p2 = next_num(n);
        
        while (p1 != p2) {
            p1 = next_num(p1);
            p2 = next_num(next_num(p2));
        }
        
        return p1 == 1;
    }
};