function exist(board: string[][], word: string): boolean {
  if (word.length === 0) return false;

  let res = false;
  // bfs for adjacency matrix
  const dfs = (r: number, l: number, i: number) => {
    if (!res) {
      if (r >= board.length || r < 0 || l >= board[0].length || l < 0 || board[r][l] !== word[i]) return;
      if (i === word.length - 1) {
        res = true;
        return res;
      }
      board[r][l] = '';
      dfs(r + 1, l, i + 1);
      dfs(r, l + 1, i + 1);
      dfs(r - 1, l, i + 1);
      dfs(r, l - 1, i + 1);
      board[r][l] = word[i];
      return;
    }
  };

  // return word if found, move to the next start if not
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[0].length; j++) {
      dfs(i, j, 0);
      if (res) return res;
    }
  }
  // return default
  return res;
}
