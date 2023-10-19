object Solution {
def findMedianSortedArrays(nums1: Array[Int], nums2: Array[Int]): Double = {
        if (
          nums1.length < 0 || nums1.length > 1000 ||
          nums2.length < 0 || nums2.length > 1000
        ) {
          throw new IllegalArgumentException("Arrays must be greater than 0 in length but less than 1000")
        }

        if (nums1.length + nums2.length > 2000)
          throw new IllegalArgumentException("Both arrays combined cannot be greater than 2000 in length")

        val max = Math.pow(10, 6)

        if (
          !nums1.forall(n => n > -max && n < max) ||
          !nums2.forall(n => n > -max && n < max)
        ) {
          throw new IllegalArgumentException("Invalid number value in array")
        }

        val sorted = (nums1 ++ nums2).sorted.toList
        val midIndex = sorted.length.toDouble / 2

        // If half of the length is a whole number
        // the median needs to be the average of the two middle numbers
        if (midIndex.isValidInt) {
          val asInt = midIndex.toInt
          (sorted(asInt - 1) + sorted(asInt)).toDouble / 2
        } else {
          // Otherwise use the middle index number
          sorted(midIndex.toInt)
        }
    }
}