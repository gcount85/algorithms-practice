function solution(maps) {
  const m = maps.length;
  const n = maps[0].length;
  let answer = Infinity;
  let parent = new Map();
  parent.set(`0,0`, 1);

  function dfs_visit(x, y, level) {
    if (x === m - 1 && y === n - 1) {
      return (answer = Math.min(level, answer));
    }

    const directions = [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1],
    ];
    for (const [dx, dy] of directions) {
      const newX = x + dx;
      const newY = y + dy;
      const key = `${newX},${newY}`;

      if (
        newX < 0 ||
        newY < 0 ||
        newX >= m ||
        newY >= n ||
        parent.get(key) === 1 ||
        !maps[newX][newY]
      )
        continue;

      parent.set(key, 1);
      dfs_visit(newX, newY, level + 1);
      parent.delete(key);
    }
  }

  dfs_visit(0, 0, 1);
  return answer === Infinity ? -1 : answer;
}

const maps = [
  [1, 0, 1, 1, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 1],
  [1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1],
];

console.log(solution(maps));
