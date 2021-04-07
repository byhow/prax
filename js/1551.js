/**
 * @param {number} n
 * @return {number}
 */
 var minOperations = function(n) {
    if (n & 1) {
        return (n - 1) / 2 * ((n - 1) /2 + 1)
    }
    return n * n /4
    
};