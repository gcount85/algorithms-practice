// 연결요소 찾는 문제 100점
function solution(n, computers) {
  let visited = new Map();

  let count = 0;

  function dfs_visit(s) {
    visited.set(s, 1);
    for (let dest = 0; dest < n; dest++) {
      if (!computers[s][dest] || visited.has(dest)) {
        continue;
      }
      dfs_visit(dest);
    }
  }

  // 모든 노드들에 대해서 dfs_visit 진행해보고 카운트
  for (let i = 0; i < n; i++) {
    if (visited.has(i)) {
      continue;
    }

    dfs_visit(i);
    count++;
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
