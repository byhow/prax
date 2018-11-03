// https://www.hackerrank.com/challenges/c-tutorial-conditional-if-else/problem?h_r=next-challenge&h_v=zen


#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    if (n >= 1 && n <= 9) {
        if (n == 1) { printf("one"); }
        else if (n == 2) { printf("two"); }
        else if (n == 3) { printf("three"); }
        else if (n == 4) { printf("four"); }
        else if (n == 5) { printf("five"); }
        else if (n == 6) { printf("six"); }
        else if (n == 7) { printf("seven"); }
        else if (n == 8) { printf("eight"); }
        else { printf("nine"); }
    } else if (n > 9){
        printf("Greater than 9");
    } else {}

    // Write Your Code Here

    return 0;
}

