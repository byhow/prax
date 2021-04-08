/**
 * @param {string} s
 * @return {boolean}
 */
 var halvesAreAlike = function(s) {
    let arr1 = s.split('')
    let set1 = new Set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    let arr2 = arr1.splice(arr1.length/2)
    console.log(arr1, arr2)
    let red = (acc, cur) => acc + (set1.has(cur) ? 1:0)
    return arr1.reduce(red, 0) === arr2.reduce(red, 0)
};