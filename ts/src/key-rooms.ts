function canVisitAllRooms(rooms: number[][]): boolean {
  const visited = Array(rooms.length).fill(false);
  function dfs(idx: number) {
    visited[idx] = true;
    rooms[idx].forEach((i) => !visited[i] && dfs(i));
  }

  dfs(0);

  return visited.every((i) => !!i);
}
