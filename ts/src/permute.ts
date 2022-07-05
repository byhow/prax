function permute(nums: number[]): number[][] {
  const list: number[][] = [];
  backtrack(list, [], nums);
  return list;
}

const backtrack = (list: number[][], tempList: number[], nums: number[]) => {
  if (tempList.length === nums.length) {
    list.push([...tempList]);
  } else {
    for (let i = 0; i < nums.length; i++) {
      if (tempList.indexOf(nums[i]) !== -1) {
        continue;
      }
      tempList.push(nums[i]);
      backtrack(list, tempList, nums);
      tempList.pop();
    }
  }
};
