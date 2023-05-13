// 연결요소 찾는 문제
function solution(n, computers) {
  const row = computers.length;
  const col = computers[0].length;
  let visited = new Array(row).fill().map(() => {
    return new Array(col).fill(0);
  });

  // console.log(visited);
  let count = 0;

  function dfs_visit(x, y) {
    const edge = [
      [x + 1, y],
      [x - 1, y],
      [x, y + 1],
      [x, y - 1],
    ];
    for (const [newX, newY] of edge) {
      if (
        newX >= 0 &&
        newY >= 0 &&
        newX < row &&
        newY < col &&
        computers[newX][newY] === 1 &&
        visited[newX][newY] === 0
      ) {
        visited[newX][newY] = 1;
        dfs_visit(newX, newY);
      }
    }
  }

  // 모든 노드들에 대해서 dfs_visit 진행해보고 카운트
  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (visited[i][j] === 1 || computers[i][j] === 0) {
        continue;
      }
      visited[i][j] = 1;
      dfs_visit(i, j);
      count++;
    }
  }

  return count;
}

n = 3;
computers = [
  [1, 1, 0],
  [1, 1, 0],
  [0, 0, 1],
];

console.log(solution(n, computers));
