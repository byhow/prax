function kidsWithCandies(candies: number[], extraCandies: number): boolean[] {
    const maxNum = Math.max(...candies);
    const result: boolean[] = []
    for (const candy of candies) {
        if (candy + extraCandies >= maxNum) {
            result.push(true)
        } else {
            result.push(false)
        }
    }
    return result
};

