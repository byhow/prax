
#include <cctype>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>

std::string solution(std::string parentheses) {
    // Type your solution here
    std::stack<char> s; 
    char tmp; 
    int left = 0;
    // Traversing the Expression 
    for (int i=0; i < parentheses.length(); i++) 
    { 
        if (parentheses[i]=='(') 
        { 
            s.push(parentheses[i]); 
            continue; 

        } else {
            tmp = s.top();
            s.pop();
            if (tmp != '(') left += 1;
        }
    } 
    int right = static_cast<int> (s.size());
    parentheses = std::string(left, '(') + parentheses + std::string(right, ')');
    return parentheses; 
}

int main(){
    std::string ret = "((()))";
    std::cout << solution(ret);
}