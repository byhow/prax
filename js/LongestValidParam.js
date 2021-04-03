/**
 * @param {string} s
 * @return {number}
 */
 var longestValidParentheses = function(s) {
    let maxP = 0, stack = []
    stack.push(-1)
    for (let i = 0; i < s.length; i++) {
        if (s[i] == "(") {
            stack.push(i)
        } else {
            let l = stack.pop()
            if (!stack.length) {
                stack.push(i)
            } else {
                maxP = Math.max(maxP, i - stack[stack.length-1])
            }
        }
    }
    
    return maxP
};