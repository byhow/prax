object Solution {
    def threeSum(nums: Array[Int]): List[List[Int]] = {
        val sortedNums = nums.sorted
        var result: List[List[Int]] = List()

        for (i <- 0 until sortedNums.length - 2) {
            if (i == 0 || (i > 0 && sortedNums(i) != sortedNums(i - 1))) {
                var left = i + 1
                var right = sortedNums.length - 1
                val target = -sortedNums(i)

                while (left < right) {
                    if (sortedNums(left) + sortedNums(right) == target) {
                        result = List(sortedNums(i), sortedNums(left), sortedNums(right)) :: result

                        while (left < right && sortedNums(left) == sortedNums(left + 1))
                            left += 1
                        while (left < right && sortedNums(right) == sortedNums(right - 1))
                            right -= 1

                        left += 1
                        right -= 1
                    } else if (sortedNums(left) + sortedNums(right) < target)
                        left += 1
                    else
                        right -= 1
                }
            }
        }

        result.reverse
    }
}
