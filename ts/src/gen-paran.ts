function generateParenthesis(n: number): string[] {
  function dfs(left: number, right: number, str: string) {
    if (str.length == n * 2) {
      res.push(str);
      return;
    }
    if (left < n) {
      dfs(left + 1, right, str.concat('('));
    }
    if (right < left) {
      dfs(left, right + 1, str.concat(')'));
    }
  }
  const res: string[] = [];
  dfs(0, 0, '');
  return res;
}
