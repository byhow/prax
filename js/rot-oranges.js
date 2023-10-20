function orangesRotting(grid) {
  let q = [], orange = 0, time = 0;

  for (let r = 0; r < grid.length; r++) {
    for (let c = 0; c < grid[r].length; c++) {
      if (grid[r][c] === 1) orange++;
      else if (grid[r][c] === 2) q.push([r, c, 0]);
    }
  }

  const dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
  const endR = grid.length - 1, endC = grid[0].length - 1;

  while (q.length && orange) {
    const [curR, curC, mins] = q.shift()

    if (grid[curR][curC] === 1) {
      grid[curR][curC] = 2;
      orange--;
      time = mins;
    }

    for (const [addR, addC] of dirs) {
      const [r, c] = [curR + addR, curC + addC]

      if (r < 0 || r > endR || c < 0 || c > endC) continue;

      if (grid[r][c] === 1) {
        q.push([r, c, mins + 1])
      }

    }
  }
  return orange ? -1 : time;
};