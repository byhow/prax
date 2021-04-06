/**
 * @param {number[]} A
 * @return {boolean}
 */
 var isIdealPermutation = function(A) {
    let cmax = 0
    for (let i = 0; i < A.length - 2; i++) {
        cmax = Math.max(cmax, A[i])
        if (cmax > A[i+2]) {
            return false
        }
    }
    return true
};