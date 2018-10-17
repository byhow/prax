#include <iostream>
#include <cstdio>
using namespace std;
// https://www.hackerrank.com/challenges/c-tutorial-basic-data-types/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

int main() {
    // Complete the code.
    int a;
    long b;
    char c;
    float d;
    double e;
    scanf("%d %ld %c %f %lf", &a, &b, &c, &d, &e);
    printf("%d\n%ld\n%c\n%.3f\n%.9lf\n", a, b, c, d, e);
    return 0;
}