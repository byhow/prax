// Binary search approach, but can be optimized with golden-section search on unimodal array

#include <vector>
using namespace std;
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        int r = A.size() - 1, mid = 0, l = 0;
        while (l < r){
            mid = (l + r) / 2;
            if (A[mid] < A[mid + 1]) l = mid;
            else if (A[mid - 1] > A[mid]) r = mid;
            else return mid;
        }
    }
};