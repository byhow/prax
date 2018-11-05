#include <iostream>

class Solution {
public:
    int reverse(int x) {
        long result = 0;

        while(x != 0)
        {
            result = result*10 + x % 10;
            x /= 10;
        }

        return (result > INT_MAX || result < INT_MIN)? 0 : result;
    }
    // int reverse(int x) {
    //     // 123
    //     // 321
    //     bool pos = true;
    //     if (x < 0) {
    //         pos = false;
    //         x = (0 - x);
    //     }

    //     int i = 1; // 100
    //     while (x / i > 1) { i = i * 10; }
    //     int ret = 0, cur = 1; 

    //     while (i != 0) {
    //         // printf("i is %d\n", i);// cur 10
    //         ret += cur * (x / i); // 1
    //         // printf("ret is %d\n", ret);
    //         x = x - (x / i) * i;
    //         // printf("x is %d\n", x);
    //         cur = cur * 10;
    //         // printf("cur is %d\n", cur);
    //         i = i / 10;
    //     }

    //     if (!pos) return ret * -1;
    //     else return ret;
    // }
};