function find132pattern(nums) {
  let stack = [];
  let third = Number.MIN_SAFE_INTEGER;
  for (let i = nums.length - 1; i >= 0; i--) {
    if (nums[i] < third) {
      return true;
    }
    while (stack.length && stack[stack.length - 1] < nums[i]) {
      third = stack.pop() || 0;
    }
    stack.push(nums[i]);
  }
  return false;
}
