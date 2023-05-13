// 69.9 점
function solution(maps) {
  const m = maps.length;
  const n = maps[0].length;
  let visited = new Array(m).fill().map(() => new Array(n).fill(0));
  let answer = Infinity; // 10000에서 infinity 로 변경

  dfs_visit(0, 0, 1);

  // level을 매개변수로 추가
  function dfs_visit(posX, posY, level) {
    if (posX === m - 1 && posY === n - 1) {
      answer = Math.min(level, answer);
      return;
    }

    const edge = [
      [posX + 1, posY],
      [posX - 1, posY],
      [posX, posY + 1],
      [posX, posY - 1],
    ];

    for (let i = 0; i < 4; i++) {
      let [x, y] = edge[i];

      if (x < 0 || y < 0) {
        continue;
      }
      if (x > m - 1 || y > n - 1) {
        continue;
      }
      if (visited[x][y] === 1) {
        continue;
      }
      if (!maps[x][y]) {
        continue;
      }
      visited[x][y] = 1;
      dfs_visit(x, y, level + 1);
      visited[x][y] = 0; // Backtrack
    }
  }

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
