function isMonotonic(nums: number[]): boolean {
  let isIncreasing = true;
  let changed = 0;
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] > nums[i - 1]) {
      isIncreasing = true;
      break;
    } else if (nums[i] < nums[i - 1]) {
      isIncreasing = false;
      break;
    }
  }
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] >= nums[i - 1] && isIncreasing) {
      continue;
    } else if (nums[i] <= nums[i - 1] && !isIncreasing) {
      continue;
    } else {
      return false;
    }
  }
  return true;
}
