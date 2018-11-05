#include <iostream> 
#include <stack> 
#include <map>
using namespace std;
class Solution {
public:
    bool isValid(string s) {
        stack<int> stack;
        map<char, char> map = {{')', '('}, {'}', '{'}, {']', '['}};
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '{' || s[i] == '(' || s[i] == '[')
                stack.push(s[i]);
            if (s[i] == '}' || s[i] == ')' || s[i] == ']') {
                if (stack.empty() || stack.top() != map[s[i]]) return false;
                stack.pop();
            }
        }
        if (!stack.empty()) return false;
        return true;

    }
};