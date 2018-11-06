#include <stdio.h>
#include <stdlib.h>
using namespace std;

void update(int *a,int *b) {
    // Complete this function    
    int c = *a;
    int tmp = abs(c - (*b));
    *a = *a + *b;
    *b = tmp;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}