#include <iostream>
#include <cstdio>
using namespace std;

void solution() {
    // int i, c, b;
    string a[11]={"even", "odd", "one", "two", 
        "three", "four", "five", "six", "seven", "eight", "nine"};
    // cin >> c >> b;
    for(int i = 0;i <= 8;i++)
    {
        if ((i > 9) && (i % 2 == 0)) {
            cout << a[0] << endl;
        } else if ((i > 9) && (i % 2 != 0)) {
            cout << a[1] << endl;
        } else {
            cout<<a[i+1]<<endl;
        }
    }
}