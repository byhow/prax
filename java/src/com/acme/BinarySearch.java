package com.acme;

public class BinarySearch {

    public int bsearch(int arr[], int x) {
        int l = 0, r = arr.length - 1;

        while(l<=r) {
            int m = l+(r-l)/2;

            if (arr[m] < x){
                l = m + 1;
            } else if(arr[m]>x){
                r = m - 1;
            } else {
                return m;
            }
        }
        return -1;
    }
}
