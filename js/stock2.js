/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let maxP = 0
    for (let i = 0; i< prices.length; i++) {
        if (prices[i] > prices[i-1]) {
            maxP += prices[i] - prices[i-1]
        }
    }
    return maxP
};
