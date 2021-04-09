/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if (digits.length == 0) {
        return []
    }
    letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    
    let backTrack = (ind, path) => {
        if (path.length == digits.length) {
            combination.push(path.join(''))
            return 
        }
        cur = letters[digits[ind]]
        
        for (let i of cur) {
            path.push(i)
            backTrack(ind +1, path)
            path.pop()
        }
    }
    let combination = []
    backTrack(0,[])
    return combination
};
