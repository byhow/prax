function orangesRotting(grid: number[][]): number {
  if (grid.length === 0) {
    return -1;
  }
  const todos = [];
  let time_elapsed = 0;
  let freshCnt = 0;

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] === 2) {
        todos.push([i, j]);
      } else if (grid[i][j] === 1) {
        freshCnt++;
      }
    }
  }

  while (todos.length > 0 && freshCnt > 0) {
    time_elapsed++;
    const cur_len = todos.length;

    for (let i = 0; i < cur_len; i++) {
      const idx: number[] = todos.shift()!;
      const [x, y] = [idx[0], idx[1]];
      const fdir = [
        [0, 1],
        [1, 0],
        [-1, 0],
        [0, -1],
      ] as const;
      for (const [dx, dy] of fdir) {
        const xx = x + dx;
        const yy = y + dy;
        if (xx >= 0 && xx < grid.length && yy >= 0 && yy < grid[0].length && grid[xx][yy] === 1) {
          grid[xx][yy] = 2;
          freshCnt--;
          todos.push([xx, yy]);
        }
      }
    }
  }

  return freshCnt === 0 ? time_elapsed : -1;
}
