void reverseStr( char* str, int size) {
    int p1 = 0, p2 = size - 1;
    
    while (p1 < p2) {
        char tmp = str[p1];
        str[p1] = str[p2];
        str[p2] = tmp;
        p1++;
        p2--;
    }

}