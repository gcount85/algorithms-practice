function solution(numbers, target) {
  let answer = 0;
  dfs_visit(0, 0);

  function dfs_visit(level, sum) {
    if (level === numbers.length) {
      if (sum === target) {
        answer += 1;
      }
      return;
    }

    // 덧셈을 먼저 하고 백트래킹 할 때마다 빼기 진행
    dfs_visit(level + 1, sum + numbers[level]);
    dfs_visit(level + 1, sum - numbers[level]);
  }

  return answer;
}
