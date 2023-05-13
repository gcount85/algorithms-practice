// 100점
function solution(maps) {
  const m = maps.length;
  const n = maps[0].length;
  let visited = new Array(m).fill().map(() => new Array(n).fill(false));

  const queue = [[0, 0, 1]]; // x, y, level
  visited[0][0] = true;
  const directions = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
  ];

  while (queue.length > 0) {
    const [x, y, level] = queue.shift(); // popleft

    if (x === m - 1 && y === n - 1) {
      return level;
    }

    for (let i = 0; i < 4; i++) {
      const newX = x + directions[i][0];
      const newY = y + directions[i][1];

      if (
        newX >= 0 &&
        newY >= 0 &&
        newX < m &&
        newY < n &&
        maps[newX][newY] === 1 &&
        !visited[newX][newY]
      ) {
        visited[newX][newY] = true;
        queue.push([newX, newY, level + 1]);
        // BFS는 최단거리 보장 -> unmarking 할 필요 X
      }
    }
  }

  return -1;
}

const maps = [
  [1, 0, 1, 1, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 1],
  [1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1],
];

console.log(solution(maps));
