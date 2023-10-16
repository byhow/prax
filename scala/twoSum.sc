import scala.collection.mutable.{HashMap}

object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
        val d = HashMap[Int, Int]()
        val n = nums.length
        for (i <- 0 until n) {
            val comp = target - nums(i)
            if (d.contains(comp)) {
                return Array(d(comp), i)
            }
            d(nums(i)) = i
        }
        Array.empty[Int]
    }
}
