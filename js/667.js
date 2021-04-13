/**
 * @param {number} n
 * @param {number} k
 * @return {number[]}
 */
 var constructArray = function(n, k) {
    let ans = []
    for (let i = 1; i < n-k; i++) {
        ans.push(i)
    }
    for (let i = 0; i < k +1 ; i++) {
        if (i % 2 == 0) {
            ans.push(n - k + Math.floor(i/2))
        } else {
            ans.push(n - Math.floor(i/2))
        }
    }
    return ans
        
};